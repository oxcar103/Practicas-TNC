#!/usr/bin/env python

# Tabla de exponentes: exponente -> polinomio
EXP = {
0x0: 0b0000, 0x1: 0b0010, 0x2: 0b0100, 0x3: 0b1000,
0x4: 0b0011, 0x5: 0b0110, 0x6: 0b1100, 0x7: 0b1011,
0x8: 0b0101, 0x9: 0b1010, 0xA: 0b0111, 0xB: 0b1110,
0xC: 0b1111, 0xD: 0b1101, 0xE: 0b1001, 0xF: 0b0001}
EXP_INV = {}    # Su inversa: polinomio -> exponente

# Tabla de la función de substitución
SUB = {
0b0000: 0b0011, 0b0001: 0b1000, 0b0010: 0b1111, 0b0011: 0b0111,
0b0100: 0b0001, 0b0101: 0b0010, 0b0110: 0b1011, 0b0111: 0b000,
0b1000: 0b1100, 0b1001: 0b1110, 0b1010: 0b1010, 0b1011: 0b0110,
0b1100: 0b1001, 0b1101: 0b1101, 0b1110: 0b0101, 0b1111: 0b0100}
SUB_INV = {}    # Tabla de la función inversa de substitución

# Rellenamos las tablas inversas
for i in EXP:
    EXP_INV[EXP[i]] = i
    SUB_INV[SUB[i]] = i

# Definición del producto en el cuerpo usando las tablas de exponentes
def Prod(a, b):
    # Si un polinomio es 0...
    if a == 0 or b == 0:
        # El producto es 0
        return 0
    # Si no...
    else:
        # El exponente del producto es la suma de los exponentes de los factores
        exp = EXP_INV[a] + EXP_INV[b]

        # Hacemos módulo los exponentes no nulos
        if exp >= len(EXP):
            exp = exp % len(EXP) + 1

        # Devolvemos el polinomio
        return EXP[exp]

# Nótese que en las siguientes funciones trabajaremos por lista con la matriz:
#      | a[0]  a[2] |
#  a = | a[1]  a[3] |

# Función de Substitución
def SubBytes(a):
    # Sustituimos cada valor por su correspondiente valor
    return [SUB[a[0]], SUB[a[1]], SUB[a[2]], SUB[a[3]]]

# Función Inversa de Substitución
def SubBytesInv(a):
    # Sustituimos cada valor por su correspondiente valor
    return [SUB_INV[a[0]], SUB_INV[a[1]], SUB_INV[a[2]], SUB_INV[a[3]]]

# Función de Rotación de Filas
def ShiftRows(a):
    # Permutamos la segunda fila de la matriz A
    return [a[0], a[3], a[2], a[1]]

# Función de Mezcla de Columnas
def MixColumns(a):
    # Creamos la matriz C
    C = [0b0011, 0b0010, 0b0010, 0b0011]

    # Multiplicamos la matriz C por la matriz A
    return [Prod(a[0], C[0])^Prod(a[1], C[2]), Prod(a[0], C[1])^Prod(a[1], C[3]), Prod(a[2], C[0])^Prod(a[3], C[2]), Prod(a[2], C[1])^Prod(a[3], C[3])]

# Función de Combinación con la Clave
def AddRoundKey(k, a):
    # Sumamos las matrices K y A
    return [k[0]^a[0], k[1]^a[1], k[2]^a[2], k[3]^a[3]]

# Generación de Claves de Ronda
def GenerateKeys(k):
    # Tomamos la clave k como lista inicial
    w = k

    # Vamos rellenando la lista...
    for i in range(4, 12):
        # Caso especial, i = 4:
        if i == 4:
            w = w + [w[0]^SUB[w[3]]^0b0001]
        # Caso especial, i = 8:
        elif i == 8:
            w = w + [w[4]^SUB[w[7]]^0b0010]
        # Caso general:
        else:
            w = w + [w[i-4]^w[i-1]]

    # Devolvemos la lista
    return w

# Algoritmo de cifrado de MiniAES
def EncMiniAES(k, a):
    # Generamos las claves
    w = GenerateKeys(k)
    k0=w[0:4]
    k1=w[4:8]
    k2=w[8:12]

    # Devolvemos el resultado
    return AddRoundKey(k2, ShiftRows(SubBytes(AddRoundKey(k1, MixColumns(ShiftRows(SubBytes(AddRoundKey(k0, a))))))))

# Algoritmo de descifrado de MiniAES
def DecMiniAES(k, a):
    # Generamos las claves
    w = GenerateKeys(k)
    k0=w[0:4]
    k1=MixColumns(w[4:8])
    k2=w[8:12]

    # Devolvemos el resultado
    return AddRoundKey(k0, ShiftRows(SubBytesInv(AddRoundKey(k1, MixColumns(ShiftRows(SubBytesInv(AddRoundKey(k2, a))))))))

