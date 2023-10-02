"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    primes = []
    Break = False
    
    for number in range(number_of_primes):
        for multiple in range(2, number):
            if number != multiple and number % multiple == 0:
                Break = True
                break
        if Break: 
            Break = False
            continue
        primes.append(number)
        
    return primes


print(primes(20))