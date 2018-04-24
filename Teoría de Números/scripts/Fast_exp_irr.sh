#! /bin/bash

# Parámetros del programa:
rat=$1                                          # Primer parámetro: componente racional
irr=$2                                          # Segundo parámetro: componente irracional
root=$3                                         # Tercer parámetro: interior de la raíz
exp=$4                                          # Cuarto parámetro: exponente
mod=$5                                          # Quinto parámetro: módulo

digits=`echo "obase=2; $exp" | bc | fold -w1`   # Convertimos el exponente a binario y con los dígitos separados
acu_rat=1
acu_irr=0
c_exp=0

prod(){
    a=$1
    b=$2
    c=$3
    d=$4
    e=$5
    let prod_rat=a*c+b*d*e
    let prod_irr=a*d+b*c
}

for i in $digits                                # Recorremos cada dígito
do
    # Elevamos al cuadrado y hacemos módulo
    prod $acu_rat $acu_irr $acu_rat $acu_irr $root        
    let acu_rat=prod_rat%mod
    let acu_irr=prod_irr%mod
    let c_exp=2*c_exp                           # Duplicamos el exponente

    # Si el dígito actual es 1...
    if (( $i == 1))
    then
        # Multiplicamos además por la base
        prod $acu_rat $acu_irr $rat $irr $root        
        let acu_rat=prod_rat%mod
        let acu_irr=prod_irr%mod
        let c_exp=c_exp+1                       # Sumamos 1 al exponente
    fi

    # Devolvemos el valor y exponente actuales
    echo "acu_rat = $acu_rat, acu_irr = $acu_irr, exp = $c_exp"

    # Escribimos el archivo de comunicación con Lucas_Suc_Fast.sh
    echo -n "$acu_rat,$acu_irr,$c_exp " >> tmp.txt
done

