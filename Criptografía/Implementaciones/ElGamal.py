#!/usr/bin/env python

from Utils import FastExp
from BabyStep_GiantStep import BabyGiant
from Silver_Pohlig_Hellman import SilverPohligHellman
from random import randint

# Parámetros del cifrado
base = -1
gen = -1
private = -1
public = -1

# Función generadora de claves a partir de la base y el generador
def GenKeysElGamal(n, b):
    # Notificamos que vamos a modificar las variables globales
    global base, gen, private, public

    base = n
    gen = b
    private = randint(2, base-2)
    public = FastExp(gen, private, base)

# Algoritmo de cifrado de ElGamal
def EncElGamal(m):
    # Si los parámetros de cifrado no están establecidos, fijamos unos
    if base == -1:
        GenKeysRSA(103, 7)    

    k = randint(2, base-2)

    # Devolvemos el resultado
    return (FastExp(gen, k, base), m * FastExp(public, k, base))

# Algoritmo de descifrado de ElGamal
def DecElGamal(c):
    # Si los parámetros de descifrado no están establecidos, fijamos unos
    if base == -1:
        GenKeysElGamal(103, 7)

    # Devolvemos el resultado
    return c[1] * FastExp(c[0], base-1-private, base) % base

# Descifrar usando Baby Step - Giant Step (true) o Silver Pohlig Hellman (false)
def BreakElGamal(c, mode_bg):
    if mode_bg:
        a = BabyGiant(base, gen, public)
    else:
        a = SilverPohligHellman(base, gen, public)

    # Devolvemos los dos divisores de la base
    return c[1] * FastExp(c[0], base-1-a, base) % base

GenKeysElGamal(211, 3)
print(DecElGamal(EncElGamal(103)))
for bg_mode in [True, False]:
    print(BreakElGamal((154, 15), bg_mode))


