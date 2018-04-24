#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en dos factores

# Calculamos la distancia al cuadrado perfecto inferior
s=`echo "sqrt($n)" | bc`
r=`echo "$s^2-$n" | bc`

# Si es 0...
if [ $r -eq "0" ]
then
    echo "$n = $s·$s"                           # Es un cuadrado perfecto y lo mostramos

# Si no...
else

    # Valores iniciales:
    let s=s+1
    r=`echo "$s^2-$n" | bc`                     # Diferencia de cuadrados: r = x^2-y^2-n
    u=`echo "2*$s+1" | bc`                      # Asociado a x: u = 2x+1
    v=1                                         # Asociado a y: v = 2y+1

    i=1                                         # Contador

    # Hasta que sea 0...
    until [ $r -eq "0" ]
    do
        # Si es mayor que 0...
        if [ $r -gt "0" ]
        then
            # Incrementamos v y ajustamos
            let r=r-v                           # Diferencia de cuadrados: r = x^2-(y+1)^2-n
            let v=v+2                           # Incrementar y: y = y+1

        # Si es menor que 0...
        elif [ $r -lt "0" ]
        then
            # Incrementamos u y ajustamos
            let r=r+u                           # Diferencia de cuadrados: r = (x+1)^2-y^2-n
            let u=u+2                           # Incrementar x: x = x+1
        fi

        let i=i+1                               # Contamos los pasos
    done

    a=`echo "($u-$v)/2" | bc`                   # = (x-y)
    b=`echo "($u+$v-2)/2" | bc`                 # = (x+y)

    echo "$n = $a·$b"                           # Devolvemos los divisores
fi

