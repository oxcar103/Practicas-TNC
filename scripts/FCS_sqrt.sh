#! /bin/bash

# Parámetros del programa:
num=$1                                          # Primer parámetro: número

q_0=$(echo "sqrt($1)/1" | bc)                   # En el caso de querer calcular la FCS del número dado, eliminar sqrt().

# Valores iniciales
P_i=0
Q_i=1
q_i=$q_0
i=0

echo "P_$i = $P_i, Q_$i = $Q_i, q_$i = $q_i"
while (( $q_i < 2*$q_0 ))                         # Recorremos cada dígito
    do
        let P_i=q_i*Q_i-P_i
        let Q_i=(num-P_i**2)/Q_i
        let q_i=(P_i+q_0)/Q_i
        let i=i+1
        echo "P_$i = $P_i, Q_$i = $Q_i, q_$i = $q_i"
    done

