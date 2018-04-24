#! /bin/bash

# Parámetros del programa:
P=$1                                            # Primer parámetro: valor de P
Q=$2                                            # Segundo parámetro: valor de Q
n=$3                                            # Tercer parámetro: exponente

U=0                                             # U_(i-2)
u=1                                             # U_(i-1)
V=2                                             # V_(i-2)
v=$P                                            # V_(i-1)

echo "U_0 = $U, V_0 = $V"
echo "U_1 = $u, V_1 = $v"

for i in `seq 2 $n`
do
    # Calculamos V_i, U_i
    let aux_U=P*u-Q*U
    let aux_V=P*v-Q*V

    echo "U_$i = $aux_U, V_$i = $aux_V"         # Mostramos los valores

    # Establecemos los siguientes U_(i-2), U_(i-1), V_(i-2) y V_(i-1)
    U=$u
    V=$v
    u=$aux_U
    v=$aux_V
done

