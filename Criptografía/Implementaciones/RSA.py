#!/usr/bin/env python

from Utils import PrintBin, FastExp, IsPrime, gcd, ModInv
from math import sqrt, factorial
from random import randint

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

# Factorizar n conociendo phi:
def FactPhi():
    # (x-p)(x-q) = x^2 + (p+q)x + pq = x^2 + (n+1-phi)x + n = x^2 + 2b + n
    b = int((base + 1 - phi)/2)

    # Calculamos el discriminante
    delta = int(sqrt(b*b - base))

    # Devolvemos (p, q)
    return (b+delta, b-delta)

# Factorizar n conociendo d:
def FactD():
    # Almacenamos e*d-1
    m = cipher*decipher -1
    g = 1

    # Mientras el MCD calculado sea un divisor impropio...
    while g == 1 or g == base:
        # Establecemos el exponente a m
        k = m

        # Tomamos un elemento aleatorio
        a = randint(1, base-1)

        # Calculado el MCD con la base
        g = gcd(a, base)[0]
        
        # Mientras el MCD sea 1 y el exponente sea par...
        while g == 1 and k%2 == 0:
            # Dividimos el exponente entre 2
            k/=2

            # Calculamos el MCD entre a^k-1 y la base
            g = gcd(FastExp(a, k, base)-1, base)[0]
    
    # Devolvemos los dos divisores de la base
    return (g, base//g)

GenKeysRSA(2609, 9199)
print(primes, base, phi, cipher, decipher)
PrintBin(EncRSA(0xCAFE))
PrintBin(DecRSA(EncRSA(0xCAFE)))
print(Pollard())
print(FactPhi())
print(FactD())

