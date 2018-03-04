#! /bin/bash

# Parámetros del programa:
num=$1                                          # Primer parámetro: número al que calcularemos las convergentes de su raíz

./scripts/FCS_sqrt.sh $1                        # Llamamos a FCS_sqrt.sh

A=1                                             # A_(i-2)
a=`cat tmp.txt | cut -f 1 -d ' '`               # A_(i-1)
B=0                                             # B_(i-2)
b=1                                             # B_(i-1)
i=0

for q_i in `cat tmp.txt | cut -f 2- -d ' '`
    do
        let aux_A=q_i*a+A
        let aux_B=q_i*b+B
        let i=i+1
        A=$a
        B=$b
        a=$aux_A
        b=$aux_B
        echo "A_$i = $a, B_$i = $b"
    done

rm tmp.txt                                      # Archivo para el scipt FCS_sqrt.sh

