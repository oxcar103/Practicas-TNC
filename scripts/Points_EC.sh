#! /bin/bash

# Parámetros del programa:
p=$1                                            # Primer parámetro: primo
    # Parámetros de la curva elíptica: x^3 + ax^2 + bx + c
    a=${2:-0}
    b=${3:-4}
    c=${4:-0}

let points=p+1                                  # Valor incial del número de puntos

# Para cada posible valor módulo p...
for x in `seq 0 $(( p-1 ))`
do
    z=`echo "($x^3+$a*$x^2+$b*$x+$c) %$p" | bc` # Calculamos su valor y^2 = z en la curva
    s=`./scripts/Jacobi_symbol.sh $x $p`        # Calculamos su símbolo de Jacobi
    let points=points+s                         # Lo añadimos al número de puntos
done

echo $points                                    # Mostramos cuántos puntos tiene la curva elíptica
