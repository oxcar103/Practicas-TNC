#! /bin/bash

# Parámetros del programa:
P=$1                                            # Primer parámetro: valor de P
Q=$2                                            # Segundo parámetro: valor de Q
mod=$3                                          # Tercer parámetro: módulo
exp=${4:-0}                                     # Cuarto parámetro: exponente, por defecto, 0

# Si no nos han pasado un exponente, calculamos uno a partir del símbolo de Jacobi
if (( $exp == 0))
    then
        let Delta=P**2-4*Q
        symbol=`./scripts/Jacobi_symbol.sh $Delta $mod`
        let exp=mod-symbol
fi

echo $exp

digits=`echo "obase=2; $exp" | bc | fold -w1`   # Convertimos el exponente a binario y con los dígitos separados

i=0
U_lit=0
U_big=1

aux=`echo "(2*$U_big-($P)*$U_lit)%$mod" | bc`
let aux=(aux+mod)%mod

for j in $digits
    do
        aux=`echo "($U_big^2-($Q)*$U_lit^2)%$mod" | bc`

        if (( $j == 0))
        then
            let i=2*i
            U_lit=`echo "(2*$U_lit*$U_big-($P)*$U_lit^2)%$mod" | bc`
            U_big=$aux
        else
            let i=2*i+1
            U_big=`echo "($P*$U_big^2-2*$Q*$U_lit*$U_big)%$mod" | bc`
            U_lit=$aux
        fi

        aux=`echo "(2*$U_big-($P)*$U_lit)%$mod" | bc`

        let aux=(aux+mod)%mod
        let U_lit=(U_lit+mod)%mod
        let U_big=(U_big+mod)%mod

        echo "V_$i = $aux, U_$i = $U_lit"
    done
    
