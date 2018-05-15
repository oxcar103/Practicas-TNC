#!/usr/bin/env python

from Utils import PrintBin, FastExp, IsPrime, gcd, ModInv
from math import factorial

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

# Aplicamos el método P-1 de Pollard
def Pollard():
    # b inicial
    b = 2

    # MCD de la base y 2^(b!)-1
    g = gcd(base, FastExp(2, factorial(b), base) - 1)[0]

    # Hasta encontrar un MCD distinto de 1...
    while g == 1:
        # Incrementamos b
        b += 1

        #Recalculamos el MCD
        g = gcd(base, FastExp(2, factorial(b), base) - 1)[0]

    # Devolvemos (p, q)
    return (g, base//g)

GenKeysRSA(2609, 9199)
print(primes, base, phi, cipher, decipher)
PrintBin(EncRSA(0xCAFE))
PrintBin(DecRSA(EncRSA(0xCAFE)))
print(Pollard())

