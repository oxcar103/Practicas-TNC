#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en dos factores

x=1
y=1
d=1

while [ $d -eq "1" ]
do
    x=`echo "($x^2+1)%$n" | bc`
    y=`echo "($y^2+1)%$n" | bc`
    y=`echo "($y^2+1)%$n" | bc`

    res=`echo "$x-$y" | bc`
    d=`./scripts/GCD.sh ${res#-} $n`
done

if [ $d -eq $n ]
then
    echo "$n es primo"
else
    res=`echo "$n/$d" | bc`
    echo "$n = $d·$res"
fi

