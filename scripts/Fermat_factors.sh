#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer

s=`echo "sqrt($n)" | bc`
r=`echo "$s^2-$n" | bc`

if [ $r -eq "0" ]
then
    echo "$n = $s·$s"
else
    let s=s+1
    r=`echo "$s^2-$n" | bc`
    u=`echo "2*$s+1" | bc`
    v=1
    i=1

    until [ $r -eq "0" ]
    do
        if [ $r -gt "0" ]
        then
            let r=r-v
            let v=v+2
        elif [ $r -lt "0" ]
        then
            let r=r+u
            let u=u+2
        fi

        let i=i+1
    done

    a=`echo "($u+$v-2)/2" | bc`
    b=`echo "($u-$v)/2" | bc`

    echo "$n = $a·$b"
fi

