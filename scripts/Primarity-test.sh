#! /bin/bash

# Parámetros del programa:
P=$1                                            # Primer parámetro: valor de P
n=$2                                            # Segundo parámetro: número

let r=n+1
found=false                                     # No conocemos ningún elemento primitivo a priori
q=2                                             # Primer candidato

# Hasta que lo encontremos o hayamos probado todos...
until $found || [ $q -ge $r ]
do
    found=true                                  # Suponemos que es el correcto

    echo "---------------------------------------------------------"
    echo "Q = $q"
    d=`echo "$P^2-4*$q" | bc`                   # Calculamos d
    msg="d = $d"                                # Almacenamos por si acaso fuera el correcto
    sym=`./scripts/Jacobi_symbol.sh $d $n`      # Calculamos su símbolo de Jacobi

    # Si el símbolo de Jacobi es 1...
    if [ $sym -eq "1" ]
    then
        echo "Jacobi_symbol = $sym"             # Lo mostramos
        found=false                             # Lo descartamos
    # Si no...
    else
        msg+="\nJacobi_symbol = "$sym           # Almacenamos por si acaso fuera el correcto

        # Recorremos los divisores de r
        for i in `factor $r | cut -f 2 -d : | tr ' ' '\n' | sort -u | tr '\n' ' '`
        do
            exp=`echo "($n+1)/$i" | bc`
            # Vemos si U_r/e = 0 mod n con e un divisor de r
            U_e=`./scripts/Lucas_Suc_Iter.sh 1 $q $n $exp | tail -n 1 | cut -f 2 -d ,`
            v_U_e=`echo $U_e | cut -f 2 -d =`
            if [ $v_U_e -eq "0" ]
            then
                echo $U_e                       # Muestra el valor de U_e
                found=false                     # Lo descartamos
            else
                msg+="\n"`echo $U_e`            # Almacenamos por si acaso fuera el correcto
            fi
        done
    fi

    # Si es el correcto...
    if $found
    then
        echo -e $msg                            # Mostramos los valores
    else
        let q=q+1                               # Siguiente candidato
    fi
done

echo "---------------------------------------------------------"

# Resultado final
if $found
then
    echo "Aceptado Q = $q"
else
    echo "No existe Q cumpliendo las condiciones"
fi

