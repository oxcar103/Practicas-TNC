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

def EncECB(m, k):
    # Criptograma inicial
    c = []

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del mensaje...
    for i in m:
        # Añadimos el nuevo criptograma cifrando el trozo de mensaje
        c = c + [DigitsInv(EncMiniAES(k, Digits(i, 0x10)), 0x10)]

    # Devolvemos el criptograma
    return DigitsInv(c, 0x10000)

def DecECB(m, k):
    # Mensaje inicial
    m = []

    # Troceamos el criptograma y la clave en bloques
    c = Digits(c, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del criptograma...
    for i in c:
        # Restauramos el mensaje descifrando el trozo de criptograma
        m = m + [DigitsInv(EncMiniAES(k, Digits(i, 0x10)), 0x10)]

    # Devolvemos el mensaje
    return DigitsInv(m, 0x10000)

def EncOFB(m, k, IV):
    # Criptograma inicial
    c = []

    # Valor inicial
    x = IV

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del mensaje...
    for i in m:
        # Calculamos el nuevo valor
        x = DigitsInv(EncMiniAES(k, Digits(x, 0x10)), 0x10)

        # Añadimos el nuevo criptograma sumando el trozo de mensaje y el nuevo valor
        c = c + [i^x]

    # Devolvemos el criptograma
    return DigitsInv(c, 0x10000)

def DecOFB(c, k, IV):
    # Mensaje inicial
    m = []

    # Valor inicial
    x = IV

    # Troceamos el criptograma y la clave en bloques
    c = Digits(c, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del criptograma...
    for i in c:
        # Calculamos el nuevo valor
        x = DigitsInv(EncMiniAES(k, Digits(x, 0x10)), 0x10)

        # Restauramos el mensaje sumando el trozo de criptograma y el nuevo valor
        m = m + [i^x]

    # Devolvemos el mensaje
    return DigitsInv(m, 0x10000)

PrintBin(Digits(DecOFB(EncOFB(0x01234567, 33127, 0x10000), 33127, 0x10000),0x10))
