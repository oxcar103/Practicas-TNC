#! /bin/bash

# Parámetros del programa:
base=$1                                         # Primer parámetro: base
exp=$2                                          # Segundo parámetro: exponente
mod=$3                                          # Tercer parámetro: módulo

digits=`echo "obase=2; $exp" | bc | fold -w1`   # Convertimos el exponente a binario y con los dígitos separados
acu=1
c_exp=0

for i in $digits                                # Recorremos cada dígito
do
    acu=`echo "$acu^2%$mod" | bc`               # Elevamos al cuadrado y hacemos módulo
    let c_exp=2*c_exp                           # Duplicamos el exponente

    # Si el dígito actual es 1...
    if (( $i == 1))
    then
        acu=`echo "$acu*$base%$mod" | bc`       # Multiplicamos además por la base
        let c_exp=c_exp+1                       # Sumamos 1 al exponente
    fi

    echo acu = $acu, exp = $c_exp               # Devolvemos el valor y exponente actuales
done

