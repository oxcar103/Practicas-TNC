#!/usr/bin/env python

from MiniAES import EncMiniAES, DecMiniAES

# Descomposición de un número en sus dígitos devueltos como una lista
def Digits (num, base):
    # Lista inicial vacía
    digits=[]

    # Mientras el número no sea nulo
    while(num != 0):
        # Guardamos el último dígito en primera posición
        digits = [num%base] + digits

        # Reducimos el número
        num //= base

    # Devolvemos los dígitos
    return digits

# Recomposición de un número a partir de sus dígitos pasados como una lista
def DigitsInv (digits, base):
    # Valor inicial
    num=0

    # Para cada dígito...
    for i in digits:
        # Incrementamos el valor actual y sumamos el dígito
        num = num*base + i

    # Devolvemos el número
    return num

# Devuelve una lista de números como binarios de 4 cifras
def PrintBin(args):
    # Mensaje inicial vacío
    msg=""

    # Para cada número...
    for i in args:
        # Lo pasamos a binario y quitamos el 0b
        binary = bin(i).split("b")[-1][-4:]

        # Completamos con 0's
        binary = '0'*(4-len(binary))+binary

        # Lo añadimos al mensaje a mostrar
        msg+=binary + " "

    # Mostramos el mensaje
    print(msg)

# Cifrado usando Electronic CodeBook
def EncECB(k, m):
    # Criptograma inicial
    c = []

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del mensaje...
    for i in m:
        # Lo transformamos en 4 dígitos
        d_i = Digits(i, 0x10)
        while len(d_i) < 4:
            d_i = [0] + d_i

        # Añadimos el nuevo criptograma cifrando el trozo de mensaje
        c = c + [DigitsInv(EncMiniAES(k, d_i), 0x10)]

    # Devolvemos el criptograma
    return DigitsInv(c, 0x10000)

# Descifrado usando Electronic CodeBook
def DecECB(k, c):
    # Mensaje inicial
    m = []

    # Troceamos el criptograma y la clave en bloques
    c = Digits(c, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del criptograma...
    for i in c:
        # Lo transformamos en 4 dígitos
        d_i = Digits(i, 0x10)
        while len(d_i) < 4:
            d_i = [0] + d_i

        # Restauramos el mensaje descifrando el trozo de criptograma
        m = m + [DigitsInv(DecMiniAES(k, d_i), 0x10)]

    # Devolvemos el mensaje
    return DigitsInv(m, 0x10000)

# Cifrado usando Output FeedBack
def EncOFB(k, m, IV):
    # Criptograma inicial
    c = []

    # Valor inicial expresado con 4 dígitos
    x = Digits(IV, 0x10)
    while len(x) < 4:
        x = [0] + x

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del mensaje...
    for i in m:
        # Calculamos el nuevo valor
        x = EncMiniAES(k, x)

        # Añadimos el nuevo criptograma sumando el trozo de mensaje y el nuevo valor
        c = c + [i^DigitsInv(x, 0x10)]

    # Devolvemos el criptograma
    return DigitsInv(c, 0x10000)

# Descifrado usando Output FeedBack
def DecOFB(k, c, IV):
    # Mensaje inicial
    m = []

    # Valor inicial expresado con 4 dígitos
    x = Digits(IV, 0x10)
    while len(x) < 4:
        x = [0] + x

    # Troceamos el criptograma y la clave en bloques
    c = Digits(c, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del criptograma...
    for i in c:
        # Calculamos el nuevo valor
        x = EncMiniAES(k, x)

        # Restauramos el mensaje sumando el trozo de criptograma y el nuevo valor
        m = m + [i^DigitsInv(x, 0x10)]

    # Devolvemos el mensaje
    return DigitsInv(m, 0x10000)

PrintBin(Digits(DecOFB(33127, EncOFB(33127, 0x01234567, 0x10000), 0x10000),0x10))
PrintBin(Digits(DecECB(33127, EncECB(33127, 0x01234567)),0x10))
