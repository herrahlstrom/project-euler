class Prime:
    def __init__(self):
        self.primes = [2]
        self.highestprime = 2

    def is_prime(self, value):
        if value == 1:
            return True
        if value < 1:
            raise ValueError("Invalid number to test for prime")
        if self.highestprime < value:
            self.primes = list(Prime.get_primes(value * 3))
            self.highestprime = self.primes[-1]
        return value in self.primes
        
    def get_primes(until):
        a = [True] * (until+1)
        a[0] = False
        a[1] = False
        for i in range(2, len(a)):
            if a[i]:
                yield i
                j = i * 2    
                while j < len(a):
                    a[j] = False
                    j += i

    def get_prime_factors(value):
        primes = list(Prime.get_primes(value))
        min = 0
        for p in primes:
            while value % p == 0:
                yield p
                value = value // p