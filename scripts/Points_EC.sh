#! /bin/bash

# Parámetros del programa:
p=$1                                            # Primer parámetro: primo
    # Parámetros de la curva elíptica:
a=${2:-0}
b=${3:-4}
c=${4:-0}

let points=p+1

for x in `seq 0 $(( p-1 ))`
do
    z=`echo "($x^3+$a*$x^2+$b*$x+$c) %$p" | bc` # z = y^2
    s=`./scripts/Jacobi_symbol.sh $x $p`
    let points=points+s
done

echo $points
