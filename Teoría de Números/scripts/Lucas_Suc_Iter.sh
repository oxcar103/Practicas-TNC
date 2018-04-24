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

digits=`echo "obase=2; $exp" | bc | fold -w1`   # Convertimos el exponente a binario y con los dígitos separados

# Valores iniciales
i=0
U_lit=0
U_big=1

# Para cada dígito del exponente...
for j in $digits
do
    # Calculamos U_(2k+1)
    aux=`echo "($U_big^2-($Q)*$U_lit^2)%$mod" | bc`

    # Si el dígito es 0...
    if (( $j == 0))
    then
        let i=2*i                               # Actualizamos el índice

        # Calculamos U_(2k) y lo asignamos a U_lit
        U_lit=`echo "(2*$U_lit*$U_big-($P)*$U_lit^2)%$mod" | bc`
        U_big=$aux                              # Asignamos U_(2k+1) a U_big
    else
        let i=2*i+1                             # Actualizamos el índice

        # Calculamos U_(2k+2) y lo asignamos a U_big
        U_big=`echo "($P*$U_big^2-2*$Q*$U_lit*$U_big)%$mod" | bc`
        U_lit=$aux                              # Asignamos U_(2k+1) a U_lit
    fi

    # Calculamos V_i
    aux=`echo "(2*$U_big-($P)*$U_lit)%$mod" | bc`

    # Hacemos módulos
    let aux=(aux+mod)%mod
    let U_lit=(U_lit+mod)%mod
    let U_big=(U_big+mod)%mod

    echo "V_$i = $aux, U_$i = $U_lit"           # Mostramos los valores de la iteración
done
    
