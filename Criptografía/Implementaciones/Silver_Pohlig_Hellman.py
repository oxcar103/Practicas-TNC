#!/usr/bin/env python

from Utils import PrintBin, FastExp
from sympy import factorint
from sympy.ntheory.modular import crt

# Variables del algoritmo hechas globales para reutilizarlas en caso
# de querer calcular varios logaritmos en un mismo cuerpo.
BASE = 0
GEN = 0
P_FACTS = {}
ROOTS = {}

# Generamos los pasos si cambiamos de cuerpo
def GenerateSquareRoots(base, gen):
    # Establecemos las variables globales al nuevo valor
    global BASE, GEN, P_FACTS, ROOTS
    BASE = base
    GEN = gen
    
    # El orden del generador es el cardinal de todos los elementos menos el 0
    order = base-1
    
    # Calculamos los factores primos con su exponente
    P_FACTS = factorint(order)

    # Tabla con las raíces de la unidad
    ROOTS = {}

    # Rellenamos la tabla de raíces
    for i in P_FACTS:
        # Raíces p_i-ésimas
        i_roots = {}

        # Variables para rellenar ROOTS
        aux = 1
        step = FastExp(gen, order/i, base)

        # Llenamos la lista
        for j in range(i):
            i_roots[aux]=j

            # Nos ahorramos calcular potencias a cambio de un producto
            aux = aux * step % base

        # Las introducimos al resto de raíces
        ROOTS[i] = i_roots


# Algoritmo de cálculo de logaritmos Paso de bebé/Paso de Gigante
def SilverPohligHellman(base, gen, element):
    # El orden del generador es el cardinal de todos los elementos menos el 0
    order = base-1

    # Si no tenemos el generador o la base correctos...
    if base != BASE or gen != GEN:
        # Generamos las raíces que usaremos
        GenerateSquareRoots(base, gen) 

    # Lista de restos y subbases
    subbases = []
    remainders = []
    
    # Buscamos el logaritmo
    for i in P_FACTS:
        # Inicialmente el exponente es 0
        exp = 0

        # Recorremos los posibles valores en los que p_i^j es divisor de n
        for j in range(P_FACTS[i]):
            y = element * FastExp(gen, order-exp, base)
            x = ROOTS[i][FastExp(y, order/(i**(j+1)), base)]
            exp += x*i**j

        # Añadimos la ecuación con congruencias
        subbases.append(i**P_FACTS[i])
        remainders.append(exp)

    # Resolvemos el sistema de congruencias
    return crt(subbases, remainders)[0]

