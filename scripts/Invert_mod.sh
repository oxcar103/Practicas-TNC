#! /bin/bash

# Parámetros del programa:
num=$1                                          # Primer parámetro: número que invertir
p=$2                                            # Segundo parámetro: primo

num=`echo "(($num%$p)+$p)%$p" | bc`

# Si num es nulo...
if [ $num -eq "0" ]
then
    inv=0                                       # No existe el inverso

# Si no...
else
    # Buscamos el inverso a fuerza bruta...
    for i in `seq $(( p-1 ))`
    do
        prod=`echo "($num*$i)%$p" | bc`

        if [ $prod -eq "1" ]                    # Si p es primo, es único
        then
            inv=$i                              # Guardamos el inverso
        fi
    done
fi

# Devolvemos el inverso
echo $inv

