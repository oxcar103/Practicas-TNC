#! /bin/bash

# Parámetros del programa:
p=$1                                            # Primer parámetro: primo
x_e=$2                                          # Segundo parámetro: coordenada del elemento al que calcular el orden
y_e=$3                                          # Tercer parámetro: coordenada del elemento al que calcular el orden

    # Parámetros de la curva elíptica: x^3 + ax^2 + bx + c
    a=${4:-0}
    b=${5:-4}
    c=${6:-0}

# Función de suma en una curva elíptica módulo p
sum_p(){
    # Parámetros del programa: componentes de los sumandos
    x_m=$1
    y_m=$2
    x_n=$3
    y_n=$4

    # Si las coordenadas x coinciden...
    if [ $x_m -eq $x_n ]
    then

        # Si son opuestos...
        if [ $y_m -eq $y_n ]
        then
            # La suma es el punto del infinito
            x_r=0
            y_r=0

        # Si no...
        else
            # Calculamos x_r e y_r de forma apropiada
            s=`echo "(3*$x_m^2 + 2*$a*$x_m + $b) / (2*$y_m)" | bc`
            x_r=`echo "((($s^2 - $a - 2*$x_m) % $p) + $p) % $p" | bc`
            y_r=`echo "(((-($y_m + $s*($x_r - $x_m))) % $p) + $p) % $p" | bc`
        fi

    # Si no...
    else
        # Calculamos x_r e y_r de forma apropiada
        s=`echo "($y_n - $y_m) / ($x_n - $x_m)" | bc`
        x_r=`echo "((($s^2 - $a - $x_m - $x_n) % $p) + $p) % $p" | bc`
        y_r=`echo "(((-($y_m + $s*($x_r - $x_m))) % $p) + $p) % $p" | bc`
    fi

    echo "$x_r, $y_r"                           # Devolvemos x_r e y_r
}

# Preparando la expresión "bonita" (sin coeficientes nulos) de la curva
curva="y^2 = x^3"
if [ $a -ne "0" ]
then
    curva=$curva"+"$a"x^2"
fi
if [ $b -ne "0" ]
then
    curva=$curva"+"$b"x"
fi
if [ $c -ne "0" ]
then
    curva=$curva"+"$c
fi

# Valores iniciales: 1*elemento = elemento
let x_i=x_e%p
let y_i=y_e%p
i=1

# Mientras no nos devuelva el punto del infinito...
while [ $x_i -ne "0" ]
do
    element=`sum_p $x_e $y_e $x_i $y_i`         # Calculamos (i+1)*elemento
    x_i=`echo $element | cut -f 1 -d ,`
    y_i=`echo $element | cut -f 2 -d , | tr -d ' '`
    let i=i+1
done

# Mostramos el orden del elemento
echo "($x_e, $y_e) es un elemento de orden $i en la curva $curva"
