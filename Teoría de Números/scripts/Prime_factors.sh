#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en primos
lim=$(echo "sqrt($n)/1" | bc)
prime=2

echo -n "$n:"                                   # Mostramos el número a descomponer

while [ $prime -le $lim ]                       # Iteramos hasta que un valor sea el doble de q_0 porque el periodo acaba ahí (hay un teorema)
do
    # Mientras que el primo divida al número...
    while (( $n % $prime == 0 ))
    do
        echo -n " $prime"                       # Lo mostramos

        let n=n/prime                           # Quitamos ese factor
        lim=$(echo "sqrt($n)/1" | bc)           # Actualizamos el límite
    done

    # Next_prime()
    prime=$(primes $prime | head -n 2 | tail -n 1)
done

# Si no es 1...
if (( $n != 1))
then
    echo -n " $n"                               # Queda un valor que también es divisor primo
fi

echo ""
