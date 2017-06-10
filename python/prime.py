class Prime:
    def __init__(self):
        self.__primes = [2,3,5,7,11,13,17,19]
        self.__primes_max = 19
        
    def get_primes(until):
        a = [True] * (until + 1)
        a[0] = False
        a[1] = False
        for i in range(2, len(a)):
            if a[i]:
                yield i
                j = i * 2    
                while j < len(a):
                    a[j] = False
                    j += i

    def is_prime(self, value):
        if value == 1:
            return True
        if value < 1:
            raise ValueError("Invalid number to test for prime")
        if self.__primes_max < value:
            max = value * 3
            self.__primes = list(Prime.get_primes(max))
            self.__primes_max = max
        return value in self.__primes

    def get_prime_factors(value):
        primes = list(Prime.get_primes(value))
        min = 0
        for p in primes:
            while value % p == 0:
                yield p
                value = value // p