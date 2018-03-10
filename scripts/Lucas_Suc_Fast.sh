#! /bin/bash

# Parámetros del programa:
P=$1                                            # Primer parámetro: valor de P
Q=$2                                            # Segundo parámetro: valor de Q
n=$3                                            # Tercer parámetro: exponente

let Delta=P**2-4*Q                              # Calculamos Delta, el valor del interior de la raíz
let half=(n+1)/2%n                              # Calculamos el inverso de 2 módulo n
let half_P=P*half%n                             # Calculamos P/2 módulo n

echo $Delta $half $half_P

touch tmp.txt                                   # Archivo para el scipt Fast_exp_irr.sh
./scripts/Fast_exp_irr.sh $half_P $half $Delta $n $n

for j in `cat tmp.txt`
    do
        i=`echo $j | cut -f 3 -d ","`

        aux=`echo $j | cut -f 1 -d ","`
        let aux=aux*2%n
        echo -n "V_$i = $aux, "
        aux=`echo $j | cut -f 2 -d ","`
        let aux=aux*2%n
        echo "U_$i = $aux"

    done

rm tmp.txt                                      # Eliminamos el archivo temporal

