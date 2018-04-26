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

def EncOFB(m, k, IV):
    # Lista inicial de criptogramas
    c = []

    # Valor inicial
    x = IV

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 0x10000)
    k = Digits(k, 0x10)

    print(k)
    # Crear el code en bloques:
    for i in m:
        # Calculamos el nuevo valor
        x = DigitsInv(EncMiniAES(k, Digits(x, 0x10)), 0x10)

        # Añadimos el nuevo criptograma
        c = c + [i^x]

    # Devolvemos los criptogramas
    return DigitsInv(c, 0x10000)

PrintBin(Digits(DecOFB(EncOFB(0x01234567, 33127, 0x10000), 33127, 0x10000),0x10))
