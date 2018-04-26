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

PrintBin(DecMiniAES(digits(0x1234,0x10), EncMiniAES(digits(0x1234,0x10), digits(0x5678,0x10))))
