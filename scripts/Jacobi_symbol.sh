#! /bin/bash

# Parámetros del programa:
element=$1                                      # Primer parámetro: elemento
base=${2#-}                                     # Segundo parámetro: base

symbol=1
let element=element%base

echo $element, $base, $symbol

until [  $element == 0 ]
    do
        while (( $element % 2 == 0 ))
            do
                let element=element/2

                echo $element

                if (( $base % 8 == 3 || $base % 8 == 5 ))
                then
                    echo "Pasa por el OR"
                    let symbol=-symbol
                fi
            done

        aux=$base
        base=$element
        let element=aux%base

        echo $element, $base, $symbol
        if (( $element % 4 == 3 && $base % 4 == 3 ))
        then
            echo "Pasa por el AND"
            let symbol=-symbol
        fi
    done

echo "$(( base == 1 ? symbol : 0 ))"            # Operador ternario

