__author__ = 'Aristide'

def generate(n):
    primes = []

    candidateFactor = 2

    while n > 1:
        while n%candidateFactor == 0:
            primes.append(candidateFactor)
            n /= candidateFactor

        candidateFactor += 1

    return primes
