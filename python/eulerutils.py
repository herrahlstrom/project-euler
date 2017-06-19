"""
Generic helpers for Project Euler
"""

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

    def __init__(self):
        self.__primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.__primes_max = 19

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
            self.__primes = list(Prime.__get_primes(until * 2))
            self.__primes_max = until * 2


    @staticmethod
    def __get_primes(until):
        primemap = [True] * (until + 1)
        primemap[0] = False
        primemap[1] = False
        for i in range(2, len(primemap)):
            if primemap[i]:
                yield i
                j = i * 2
                while j < len(primemap):
                    primemap[j] = False
                    j += i
