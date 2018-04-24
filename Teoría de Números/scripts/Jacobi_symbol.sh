#! /bin/bash

# Parámetros del programa:
element=$1                                      # Primer parámetro: elemento
base=${2#-}                                     # Segundo parámetro: base

symbol=1
let element=(base+element%base)%base            # (element/base)=(element%base/base)

# Hasta que element sea 0...
until [  $element == 0 ]
do
    # Mientras sea par...
    while (( $element % 2 == 0 ))
    do
        let element=element/2                   # (element/base)=(2/base)*((element/2)/base)

        # Si la base es congruente a 3 ó 5 módulo 8
        if (( $base % 8 == 3 || $base % 8 == 5 ))
        then
            let symbol=-symbol                  # (2/base)=-1
        fi
    done

    # Le damos la vuelta
    aux=$base
    base=$element
    element=$aux

    # Si base y elemento son congruentes a 3 módulo 4...
    if (( $element % 4 == 3 && $base % 4 == 3 ))
    then
        let symbol=-symbol                      # (element/base)=-(base/element)
    fi

    let element=element%base                    # (element/base)=(element%base/base)
done

echo "$(( base == 1 ? symbol : 0 ))"            # Operador ternario

