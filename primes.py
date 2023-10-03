"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from math import sqrt


def primes(number_of_primes):
    primes = []
    prime = 2
    while number_of_primes >= 1:
        if isPrime(prime):
            primes.append(prime)
            number_of_primes -=1
        prime += 1
    return primes
    

def isPrime(prime):
    # check for divisibility by 2 so you dont have to check for all even numbers
    if prime % 2 == 0:
        if prime == 2:
            return True
        return False
    
    for factor in range(3, int(sqrt(prime) + 1) , 2):
        if prime % factor == 0:
            return False
    return True


print(primes(20))
