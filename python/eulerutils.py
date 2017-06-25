"""
Generic helpers for Project Euler
"""

from time import time

def permute_list(inputlist):
    """
    Create all permutations of a given list (include strings)
    """
    if len(inputlist) <= 1:
        yield inputlist
    else:
        chunk = inputlist[0]
        for item in permute_list(inputlist[1:]):
            for i in range(0, len(item)+1):
                yield item[0:i] + chunk + item[i:]

class Prime:
    """
    Prime number operations
    """

    def __init__(self, start=19):
        self.__primes = list(Prime.__get_primes(start))
        self.__primes_max = start

    def get_primes(self, until):
        """
        List all primes from 2 to a specified value
        """
        self.__ensure_primes(until)
        return [x for x in self.__primes if x <= until]

    def is_prime(self, value):
        """
        Detect if a specified value is a prime
        """
        if value < 2:
            raise ValueError("Invalid number to test for prime")
        self.__ensure_primes(value)
        return value in self.__primes

    def get_prime_factors(self, value):
        """
        Get the prime factors for a specified value
        """
        self.__ensure_primes(value)
        for prime in self.__primes:
            while value % prime == 0:
                yield prime
                value = value // prime
            if value < 2:
                break

    def __ensure_primes(self, until):
        if self.__primes_max < until:
            self.__primes = list(Prime.__get_primes(until))
            self.__primes_max = until


    @staticmethod
    def __get_primes(until):
        sieve = [True] * until
        for i in range(3, int(until**0.5)+1, 2):
            if sieve[i]:
                sieve[i*i::2*i] = [False]*((until-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3, until, 2) if sieve[i]]


class Stopwatch:
    """
    Create a stopwatch for taking elapsed times
    """
    def __init__(self):
        self.elapsed = 0
        self.current_start = None

    def start(self):
        """
        Start the stopwatch
        """
        if self.current_start is None:
            self.current_start = time()

    def stop(self):
        """
        Stop the stopwatch
        """
        if not self.current_start is None:
            self.elapsed += time() - self.current_start
            self.current_start = None

    def get_elapsed(self):
        """
        Get the current elapsed time
        """
        if self.current_start is None:
            return self.elapsed
        return self.elapsed + time() - self.current_start
        