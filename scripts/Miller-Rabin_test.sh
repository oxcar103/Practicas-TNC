#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número
p=${2:-103}                                     # Segundo parámetro: primo

let m=n-1

# Calculamos p^(n-1)
acu=`./scripts/Fast_exp_int.sh $p $m $n | tail -n 1 | cut -f 1 -d , | cut -f 2 -d =`

# Si p^m no es 1...
if [ $acu -ne "1" ]
then
    echo "No es primo"                          # No es primo

# Si no...
else
    i=0

    # Buscamos (i,m) tal que n-1 = 2^i*m con m impar
    while (( $m % 2 == 0 ))
    do
        let m=m/2
        let i=i+1
    done

    # Calculamos p^m
    acu=`./scripts/Fast_exp_int.sh $p $m $n | tail -n 1 | cut -f 1 -d , | cut -f 2 -d =`

    # Si es 1 ó -1...
    if [ $acu -eq "1" ] || [ $acu -eq $(($n-1)) ]
    then
        echo "Es primo"                         # Es primo

    # Si no...
    else
        # Mientra i > 0...
        while [ $i -gt 0 ]
        do
            acu=`echo "$acu^2%$n" | bc`         # Elevamos al cuadrado

            # Si es 1...
            if [ $acu -eq "1" ]
            then
                echo "No es primo"              # No es primo, existe una raíz de la unidad distinta de 1 ó -1
                i=0                             # Salimos del bucle, es un break

            # Si es -1...
            elif [ $acu -eq $(($n-1)) ]
            then
                echo "Es primo"                 # Es primo, realmente sólo es posible primo
                i=0                             # Salimos del bucle, es un break

            # Si no...
            else

                # Si i no es 1...
                if [ $i -eq "1" ]
                then
                    echo "No es primo"          # No es primo, ya que p^(n-1) = 1 y su raíz es distinta de 1 ó -1
                fi
                
                let i=i-1                       # Seguimos buscando
            fi
        done
    fi
fi
