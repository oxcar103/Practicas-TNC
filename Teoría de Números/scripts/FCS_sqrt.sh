#! /bin/bash

# Parámetros del programa:
num=$1                                          # Primer parámetro: número al que calcularemos el FCS de su raíz

q_0=$(echo "sqrt($1)/1" | bc)                   # En el caso de querer calcular la FCS del número dado, eliminar sqrt().

# Valores iniciales
P_i=0
Q_i=1
q_i=$q_0
i=0

echo "P_$i = $P_i, Q_$i = $Q_i, q_$i = $q_i"    # Mostramos los valores en cada iteración
echo -n "$q_i " >> tmp.txt                      # Escribimos el archivo de comunicación con Convergent.sh 

while (( $q_i < 2*$q_0 ))                       # Iteramos hasta que un valor sea el doble de q_0 porque el perido acaba ahí (hay un teorema)
do
    let i=i+1                                   # Siguiente iteración

    # Cálculo de los valores
    let P_i=q_i*Q_i-P_i
    let Q_i=(num-P_i**2)/Q_i
    let q_i=(P_i+q_0)/Q_i

    echo "P_$i = $P_i, Q_$i = $Q_i, q_$i = $q_i"
    echo -n "$q_i " >> tmp.txt                  # Escribimos el archivo de comunicación con Convergent.sh 
done

echo "" >> tmp.txt
