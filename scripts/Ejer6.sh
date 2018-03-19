#! /bin/bash

# Parámetros del programa:
P=$1                                            # Primer parámetro: valor de P
n=$2                                            # Segundo parámetro: número

let r=n+1

for q in `seq 2 20`                             # Para un puñado de Q's
    do
        echo "---------------------------------------------------------"
        echo "Q = $q"
        d=`echo "$P^2-4*$q" | bc`               # Calculamos d
        echo "d = $d"
        sym=`./scripts/Jacobi_symbol.sh $d $n`  # Calculamos su símbolo de Jacobi
        echo "Jacobi_symbol = $sym"

        # Si no es 1...
        if (( $sym != 1 ))
            then
                # Recorremos los divisores de r
                for i in `factor $r | cut -f 2 -d :`
                    do
                        exp=`echo "($n+1)/$i" | bc`
                        # Vemos si U_r/e = 0 mod n con e un divisor de r
                        ./scripts/Lucas_Suc_Iter.sh 1 $q $n $exp | tail -n 1
                    done

                # Comprobamos que U_r = 0 mod n
                ./scripts/Lucas_Suc_Iter.sh 1 $q $n | tail -n 1
        fi
done
