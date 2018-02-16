#! /bin/bash

# Parámetros del programa:
base=$1             # Primer parámetro: base
exp=$2              # Segundo parámetro: exponente
mod=$3              # Tercer parámetro: módulo

digits=`echo "obase=2; $exp" | bc | fold -w1`
acu=1
c_exp=0

for i in $digits
    do
        let acu=acu**2%mod
        let c_exp=2*c_exp

        if (( $i == 1))
        then
            let acu=acu*base%mod
            let c_exp=c_exp+1
        fi

        echo acu = $acu, exp = $c_exp
    done

