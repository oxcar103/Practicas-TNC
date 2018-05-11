#!/usr/bin/env python

from MiniAES import EncMiniAES, DecMiniAES
from Utils import Digits, DigitsInv, PrintBin

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

# Cifrado usando Cypher-Book Chaining
def EncCBC(k, m, IV):
    # Criptograma inicial
    c = [IV]

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 0x10000)
    k = Digits(k, 0x10)

    # Para cada trozo del mensaje...
    for i in m:
        # Le sumamos c_(i-1) y lo transformamos en 4 dígitos
        d_i = Digits(i^c[-1], 0x10)
        while len(d_i) < 4:
            d_i = [0] + d_i

        # Añadimos el nuevo criptograma cifrando el trozo de mensaje
        c = c + [DigitsInv(EncMiniAES(k, d_i), 0x10)]

    # Devolvemos el criptograma
    return DigitsInv(c, 0x10000)

# Descifrado usando Cypher-Book Chaining
def DecCBC(k, c):
    # Mensaje inicial
    m = []

    # Troceamos el criptograma y la clave en bloques
    c = Digits(c, 0x10000)
    (c_previous, c) = (c[0], c[1:])
    k = Digits(k, 0x10)

    # Para cada trozo del criptograma...
    for i in c:
        # Lo transformamos en 4 dígitos
        d_i = Digits(i, 0x10)
        while len(d_i) < 4:
            d_i = [0] + d_i

        # Restauramos el mensaje descifrando el trozo de criptograma
        m = m + [DigitsInv(DecMiniAES(k, d_i), 0x10)^c_previous]

        # Actualizamos c_(i-1)
        c_previous = i

    # Devolvemos el mensaje
    return DigitsInv(m, 0x10000)

# Cifrado usando Cipher FeedBack
def EncCFB(k, m, r, IV):
    # Criptograma inicial
    c = []

    # Troceamos el mensaje y la clave en bloques
    m = Digits(m, 1 << r)
    k = Digits(k, 0x10)

    # Valor inicial expresado con 4 dígitos
    x = Digits(IV, 0x10)
    while len(x) < 4:
        x = [0] + x

    # Para cada trozo del mensaje...
    for i in m:
        # Calculamos el nuevo valor
        y = EncMiniAES(k, x)

        # Añadimos el nuevo criptograma sumando el trozo de mensaje y los r dígitos más significativos del nuevo valor
        c = c + [i^(DigitsInv(y, 0x10)>>(0x10-r))]

        # Tomamos los N-r cifras más significativas y le acoplamos el trozo de criptograma c
        x = Digits((DigitsInv(x,0x10) << r) + c[-1], 0x10)[-4:]
        while len(x) < 4:
            x = [0] + x

    # Devolvemos el criptograma
    return DigitsInv(c, 1 << r)

# Descifrado usando Cipher FeedBack
def DecCFB(k, c, r, IV):
    # Mensaje inicial
    m = []

    # Troceamos el criptograma y la clave en bloques
    c = Digits(c, 1 << r)
    k = Digits(k, 0x10)

    # Valor inicial expresado con 4 dígitos
    x = Digits(IV, 0x10)
    while len(x) < 4:
        x = [0] + x

    # Para cada trozo del criptograma...
    for i in c:
        # Calculamos el nuevo valor
        y = EncMiniAES(k, x)

        # Añadimos el nuevo mensaje sumando el trozo de criptograma y los r dígitos más significativos del nuevo valor
        m = m + [i^(DigitsInv(y, 0x10)>>(0x10-r))]

        # Tomamos los N-r cifras más significativas y le acoplamos el trozo de criptograma i
        x = Digits((DigitsInv(x,0x10) << r) + i, 0x10)[-4:]
        while len(x) < 4:
            x = [0] + x

    # Devolvemos el mensaje
    return DigitsInv(m, 1 << r)

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

PrintBin(DecECB(0x8167, EncECB(0x8167, 0x01234567)))
PrintBin(DecCBC(0x8167, EncCBC(0x8167, 0x01234567, 0x0001)))
PrintBin(DecCFB(0x8167, EncCFB(0x8167, 0x01234567, 3, 0x0001), 3, 0x0001))
PrintBin(DecOFB(0x8167, EncOFB(0x8167, 0x01234567, 0x0001), 0x0001))
PrintBin(DecCFB(0x8167, EncCFB(0x8167, 0x012345678, 3, 0x0001), 3, 0x0001)) # Con padding
