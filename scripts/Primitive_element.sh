#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número

let r=n-1
found=false                                     # No conocemos ningún elemento primitivo a priori
prim=-1
a=2                                             # Primer candidato

# Hasta que lo encontremos o hayamos probado todos...
until $found || [ $a -ge $r ]
do
    found=true                                  # Suponemos que es el correcto

    # Calculamos a^(n-1) mod n
    aux=`./scripts/Fast_exp_int.sh $a $r $n | tail -n 1 | cut -f 2 -d = | cut -f 1 -d ,`

    # Si no es 1...
    if [ $aux -ne "1" ]
    then
        found=false                             # No es el correcto
    else
        # Recorremos los divisores de r
        for p_i in `factor $r | cut -f 2 -d : | tr ' ' '\n' | sort -nu | tr '\n' ' '`
            do
            exp=`echo "$r/$p_i" | bc`
            # Calculamos a^((n-1)/p_i) mod n
            aux=`./scripts/Fast_exp_int.sh $a $exp $n | tail -n 1 | cut -f 2 -d = | cut -f 1 -d ,`

            # Si es 1...
            if [ $aux -eq "1" ]
            then
                found=false                     # No es el correcto
            fi
        done
    fi

    # Si es el correcto...
    if $found
    then
        prim=$a                                 # Guardamos el elemento
    else
        let a=a+1                               # Siguiente candidato
    fi
done

# Mostramos los resultados
if [ $prim -eq "-1" ]
then
    echo "No hay elementos primitivos en Z_$n"
else
    echo "$prim es un elemento primitivo de Z_$n"
fi
