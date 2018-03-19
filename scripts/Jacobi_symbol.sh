#! /bin/bash

# Parámetros del programa:
element=$1                                      # Primer parámetro: elemento
base=${2#-}                                     # Segundo parámetro: base

symbol=1
let element=(base+element%base)%base

until [  $element == 0 ]
do
    while (( $element % 2 == 0 ))
    do
        let element=element/2

        if (( $base % 8 == 3 || $base % 8 == 5 ))
        then
            let symbol=-symbol
        fi
    done

    aux=$base
    base=$element
    element=$aux

    if (( $element % 4 == 3 && $base % 4 == 3 ))
    then
        let symbol=-symbol
    fi

    let element=element%base
done

echo "$(( base == 1 ? symbol : 0 ))"            # Operador ternario

