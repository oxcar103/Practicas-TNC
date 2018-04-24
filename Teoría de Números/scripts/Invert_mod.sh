#! /bin/bash

# Parámetros del programa:
num=$1                                          # Primer parámetro: número que invertir
p=$2                                            # Segundo parámetro: primo

num=`echo "(($num%$p)+$p)%$p" | bc`             # Hacemos módulo a la entrada
inv=0                                           # Si p es primo, existe y es único

# Si num no es nulo...
if [ $num -ne "0" ]
then
    # Valores iniciales
    prod=0
    i=0

    # Buscamos el inverso por fuerza bruta...
    while [ $inv -eq "0" ]
    do
        let prod=($prod+$num)%$p                # Valor del producto entre el número y el candidato
        let i=i+1                               # Siguiente candidato

        # Si el candidato es la identidad...
        if [ $prod -eq "1" ]
        then
            inv=$i                              # Guardamos el inverso
        fi
    done
fi

# Devolvemos el inverso
echo $inv

