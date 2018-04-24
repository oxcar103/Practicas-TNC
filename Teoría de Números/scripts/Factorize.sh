#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en factores primos
met=${2:-1}                                     # Segundo parámetro: método a usar (0, Fermat; 1, ρ de Pollard, por defecto)
num_p=${3:-5}                                   # Tercer parámetro: número de primos que verificar, por defecto 5

# Función de un paso de factorización
factor(){
    # Parámetros del programa:
    m=$1                                        # Primer parámetro: número a descomponer

    prime=true                                  # Suponemos que es primo

    for p in `primes 2 | head -n $num_p`        # Recorremos num_p primos
    do
        if [ $p -ne $m ]                        # Evitamos que nos devuelva "No primo" si seleccionamos uno pequeño
        then
            test=`./scripts/Miller-Rabin_test.sh $m $p`

            # Si no pasa el test de Miller-Rabin...
            if [ "$test" == "No es primo" ]
            then
                prime=false                     # No es primo
            fi
        fi
    done

    # Si es primo...
    if $prime
    then
        # Demostramos su primalidad dando un elemento primitivo
        msg+=`./scripts/Primitive_element.sh $m`"\n"

    # Si no...
    else
        # Usamos el método ρ de Pollard
        if [ $met -eq "1" ]
        then
            facts=`./scripts/Rho_Pollard.sh $m | cut -f 2 -d =`

        # Usamos el método de Fermat
        elif [ $met -eq "0" ]
        then
            facts=`./scripts/Fermat_factors.sh $m | cut -f 2 -d =`

        # Método incorrecto
        else
            echo "Error:"
            facts=$m
        fi

        msg+="$m = $facts\n"                    # Mostramos la descomposición
        facts=`echo $facts | tr '·' ' '`

        # Para cada factor...
        for i in $facts
        do
            factor $i $met                      # Intentamos factorizar
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

msg+="$n\n"                                     # Mostramos la primera descomposición

factor $n                                       # Intentamos factorizar el resto

echo -ne $msg                                   # Mostramos todo
