#! /bin/bash

# Parámetros del programa:
P=$1                                            # Primer parámetro: valor de P
Q=$2                                            # Segundo parámetro: valor de Q
mod=$3                                          # Tercer parámetro: módulo
exp=${4:-0}                                     # Cuarto parámetro: exponente, por defecto, 0

let Delta=P**2-4*Q                              # Calculamos Delta, el valor del interior de la raíz
let half=(mod+1)/2%mod                          # Calculamos el inverso de 2 módulo n
let half_P=(P*half%mod+mod)%mod                 # Calculamos P/2 módulo n

# Si no nos han pasado un exponente, calculamos uno a partir del símbolo de Jacobi
if (( $exp == 0))
then
    symbol=`./scripts/Jacobi_symbol.sh $Delta $mod`
    let exp=mod-symbol
fi


touch tmp.txt                                   # Archivo para el scipt Fast_exp_irr.sh
./scripts/Fast_exp_irr.sh $half_P $half $Delta $exp $mod > /dev/null

for j in `cat tmp.txt`
do
    i=`echo $j | cut -f 3 -d ","`

    aux=`echo $j | cut -f 1 -d ","`
    let aux=aux*2%mod
    echo -ne "V_$i = $aux, "
    aux=`echo $j | cut -f 2 -d ","`
    let aux=aux*2%mod
    echo "U_$i = $aux"
done

rm tmp.txt                                      # Eliminamos el archivo temporal

