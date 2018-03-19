#! /bin/bash

# Parámetros del programa:
n=$1                                            # Primer parámetro: número a descomponer en primos
lim=$(echo "sqrt($n)/1" | bc)
prime=2

echo -n "$n:" 

while [ $prime -le $lim ]                       # Iteramos hasta que un valor sea el doble de q_0 porque el perido acaba ahí (hay un teorema)
do
    while (( $n % $prime == 0 ))
    do
        echo -n " $prime"

        let n=n/prime
        lim=$(echo "sqrt($n)/1" | bc)
    done

    prime=$(primes $prime | head -n 2 | tail -n 1)
done

if (( $n != 1))
then
    echo -n " $n"
fi

echo ""
