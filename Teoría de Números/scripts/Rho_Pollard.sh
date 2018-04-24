#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en dos factores

# Valores iniciales:
x=1
y=1
d=1

# Mientras el GCD sea 1...
while [ $d -eq "1" ]
do
    # x = f(x)
    x=`echo "($x^2+1)%$n" | bc`

    # y = f(f(y))
    y=`echo "($y^2+1)%$n" | bc`
    y=`echo "($y^2+1)%$n" | bc`

    # Calculamos GCD(|x-y|, n)
    res=`echo "$x-$y" | bc`
    d=`./scripts/GCD.sh ${res#-} $n`
done

# Si es n...
if [ $d -eq $n ]
then
    echo "$n es primo"                          # Es primo, no hemos encontrado ningún divisor menor que él mismo

# Si no...
else
    res=`echo "$n/$d" | bc`                     # Calculamos el otro divisor
    echo "$n = $d·$res"                         # Mostramos ambos
fi

