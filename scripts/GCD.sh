#! /bin/bash

# Parámetros del programa:
a=$1                                            # Primer parámetro: un número
b=$2                                            # Segundo parámetro: otro número

# Algoritmo de Euclides
until [ $b -eq "0" ]
do
    aux=`echo "$b%$a" | bc`
    a=$b
    b=$aux
done

# Devolvemos el GCD(a,b)
echo $a
