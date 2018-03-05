#! /bin/bash

# Parámetros del programa:
num=$1                                          # Primer parámetro: número al que calcularemos las convergentes de su raíz

touch tmp.txt                                   # Archivo para el scipt Convergent.sh
./scripts/FCS_sqrt.sh $num                      # Llamamos a FCS_sqrt.sh

A=1                                             # A_(i-2)
a=`cat tmp.txt | cut -f 1 -d ' '`               # A_(i-1)
B=0                                             # B_(i-2)
b=1                                             # B_(i-1)
i=0

for q_i in `cat tmp.txt | cut -f 2- -d ' '`
    do
        # Calculamos A_i, B_i
        let aux_A=q_i*a+A
        let aux_B=q_i*b+B
        let i=i+1

        echo "A_$i = $aux_A, B_$i = $aux_B"     # Mostramos los valores

        # Establecemos los siguientes A_(i-2), A_(i-1), B_(i-2) y B_(i-1)
        A=$a
        B=$b
        a=$aux_A
        b=$aux_B
    done

rm tmp.txt                                      # Eliminamos el archivo temporal

