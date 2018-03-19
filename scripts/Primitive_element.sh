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
        found=true                              # Suponemos que es el correcto

        # Recorremos los divisores de r
        for i in `factor $r | cut -f 2 -d :`
            do
                exp=`echo "$r/$i" | bc`
                # Calculamos a^((n-1)/p) mod n
                aux=`./scripts/Fast_exp_int.sh $a $exp $n | tail -n 1 | cut -f 2 -d = | cut -f 1 -d ,`

                # Si es 1...
                if [ $aux -eq "1" ]
                    then
                        found=false             # No es el correcto
                fi
            done

        # Si es el correcto...
        if $found
            then
                prim=$a                         # Guardamos el elemento
        fi

        let a=a+1                               # Siguiente candidato
done

echo "$prim es un elemento primitivo de Z_$n"   # Mostramos los resultados
