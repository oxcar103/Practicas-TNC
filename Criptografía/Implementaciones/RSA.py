#!/usr/bin/env python

from Utils import PrintBin, FastExp, IsPrime, ModInv

# Parámetros del cifrado
primes = [-1, -1]
base = -1
phi = -1
cipher = -1
decipher = -1

# Función generadora de claves a partir de dos primos
def GenKeysRSA(p, q):
    # Notificamos que vamos a modificar las variables globales
    global primes, base, phi, cipher, decipher

    primes = [p, q]
    base = p*q
    phi = (p-1)*(q-1)

    # Buscamos el primer primo mayor que 11 que sea coprimo con la base
    cipher = 11
    while not IsPrime(cipher) or phi % cipher == 0:
        cipher += 2

    decipher = ModInv(cipher, phi)

# Algoritmo de cifrado de RSA
def EncRSA(m):
    # Si los parámetros de cifrado no están establecidos, fijamos unos
    if primes[0] == -1:
        GenKeysRSA(97, 103)    

    # Devolvemos el resultado
    return FastExp(m, cipher, base)

# Algoritmo de descifrado de RSA
def DecRSA(c):
    # Si los parámetros de cifrado no están establecidos, fijamos unos
    if primes[0] == -1:
        GenKeysRSA(97, 103)    

    # Devolvemos el resultado
    return FastExp(c, decipher, base)

GenKeysRSA(2609, 9199)
print(primes, base, phi, cipher, decipher)
PrintBin(EncRSA(0xCAFE))
PrintBin(DecRSA(EncRSA(0xCAFE)))

