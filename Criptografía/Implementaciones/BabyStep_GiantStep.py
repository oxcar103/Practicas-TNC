#!/usr/bin/env python

from math import sqrt, ceil
from Utils import FastExp

# Variables del algoritmo hechas globales para reutilizarlas en caso
# de querer calcular varios logaritmos en un mismo cuerpo.
BASE = 0
GEN = 0
BABY = {}
GIANT= 0

# Generados de los pasos si cambiamos de cuerpo
def GenerateBabyGiantSteps(base, gen):
    # Establecemos las variables globales al nuevo valor
    global BASE, GEN, BABY, GIANT
    BASE = base
    GEN = gen
    print(GEN, BASE)
    # Número de iteraciones
    root = ceil(sqrt(base))

    # Tabla con el paso de bebé
    BABY = {}

    # Variable para rellenar BABY
    aux = 1

    # Rellenamos la tabla
    for i in range(root):
        BABY[aux] = i

        # Nos ahorramos calcular potencias a cambio de un producto
        aux = aux * gen % base

    # Calculamos el paso de gigante
    GIANT = FastExp(gen, (base-1)-root, base)

    print(BABY, GIANT, root, base-root)



# Algoritmo de cálculo de logaritmos Paso de bebé/Paso de Gigante
def BabyGiant(base, gen, element):
    # Número de iteraciones
    root = ceil(sqrt(base))

    # Si no tenemos el generador o la base correctos...
    if base != BASE or gen != GEN:
        print(base, BASE)
        print(gen, GEN)
        # Generamos los pasos que usaremos
        GenerateBabyGiantSteps(base, gen) 

    # Buscamos el logaritmo
    for i in range(root):
        # Si está en nuestra tabla BABY...
        if element in BABY:
            # Calculamos el índice y lo devolvemos
            return BABY[element] + i*root
        #Si no...
        else:
            # Damos un paso de Gigante
            element = element * GIANT % base

    # No existe el logaritmo
    return -1

