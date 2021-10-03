"""Write an algorithm that calculates the fibonacci sequence for Fn = Fn-1 + Fn-2, where N is 1000,
and F0 = 0, and F1 = 1. Sum each number that is prime within the fibonacci sequence.

The answer will be O2F{sum_of_primes}. It will be quite long."""

from sympy import isprime


def iterativeFib(n):
    a, b = 0, 1
    j = 0
    for i in range(n):
        if isprime(b):
            j += b
        a, b = b, a + b
    return j


print(iterativeFib(1000))
