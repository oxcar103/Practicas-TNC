#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número
p=${2:-103}                                     # Segundo parámetro: primo

let m=n-1
acu=`./scripts/Fast_exp_int.sh $p $m $n | tail -n 1 | cut -f 1 -d , | cut -f 2 -d =`

if [ $acu -ne "1" ]
then
    echo "No es primo"
else
    i=0

    while (( $m % 2 == 0 ))
    do
        let m=m/2
        let i=i+1
    done

    acu=`./scripts/Fast_exp_int.sh $p $m $n | tail -n 1 | cut -f 1 -d , | cut -f 2 -d =`

    if [ $acu -eq "1" ] || [ $acu -eq $(($n-1)) ]
    then
        echo "Es primo"
    else
        while [ $i -gt 0 ]
        do
            let acu=acu**2%n

            if [ $acu -eq "1" ]
            then
                echo "No es primo"
                i=0
            elif [ $acu -eq $(($n-1)) ]
            then
                echo "Es primo"
                i=0
            else
                if [ $i -eq "1" ]
                then
                    echo "No es primo"
                fi
                
                let i=i-1
            fi
        done
    fi
fi
