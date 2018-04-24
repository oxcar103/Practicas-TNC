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
#  | a0  a2 |
#  | a1  a3 |

def SubBytes(a0, a1, a2, a3):
    # Sustituimos cada valor por su correspondiente valor
    return [SUB[a0], SUB[a1], SUB[a2], SUB[a3]]

def ShiftRows(a0, a1, a2, a3):
    # Permutamos la segunda fila de la matriz A
    return [a0, a3, a2, a1]

def MixColumns(a0, a1, a2, a3):
    # Creamos la matriz C
    C = [0b0011, 0b0010, 0b0010, 0b0011]

    # Multiplicamos la matriz C por la matriz A
    return [Prod(a0, C[0])^Prod(a1, C[2]), Prod(a0, C[1])^Prod(a1, C[3]), Prod(a2, C[0])^Prod(a3, C[2]), Prod(a2, C[1])^Prod(a3, C[3])]

def AddRoundKey(k0, k1, k2, k3, a0, a1, a2, a3):
    # Sumamos las matrices K y A
    return [k0^a0, k1^a1, k2^a2, k3^a3]

