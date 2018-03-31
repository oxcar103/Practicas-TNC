#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en factores primos
met=${2:-1}                                     # Segundo parámetro: método a usar (0, Fermat; 1, ρ de Pollard, por defecto)
num_p=${3:-5}                                   # Tercer parámetro: número de primos que verificar, por defecto 5

factor(){
    # Parámetros del programa:
    m=$1                                        # Primer parámetro: número a descomponer

    prime=true

    for p in `primes 2 | head -n $num_p`
    do
        if [ $p -ne $m ]
        then
            aux=`./scripts/Miller-Rabin_test.sh $m $p`
            if [ "$aux" == "No es primo" ]
            then
                prime=false
            fi
        fi
    done

    if $prime
    then
        msg+=`./scripts/Primitive_element.sh $m`"\n"
    else
        if [ $met -eq "1" ]
        then
            facts=`./scripts/Rho_Pollard.sh $m | cut -f 2 -d =`
        elif [ $met -eq "0" ]
        then
            facts=`./scripts/Fermat_factors.sh $m | cut -f 2 -d =`
        else
            echo "Error:"
            facts=$m
        fi

        msg+="$m = $facts\n"
        facts=`echo $facts | tr '·' ' '`

        for i in $facts
        do
            factor $i $met
        done
    fi
}

msg+="n = "

# Quitamos la paridad
while (( $n % 2 == 0 ))
    do
        n=`echo "$n/2" | bc`
        msg+="2·"
    done

msg+="$n\n"

factor $n

echo -ne $msg
