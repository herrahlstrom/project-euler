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
            self.primes = list(Prime.get_primes(value*3))
            self.highestprime = self.primes[-1]
        return value in self.primes
    
    def get_primes(until):
        sieveBound = (int(until-1))//2
        upperSqrt = (int(until**0.5)-1)//2
        bits = [True]*(sieveBound+1)
        for i in range(1, upperSqrt+1):
            if bits[i]:
                j = i * 2 * (i + 1)
                while j <= sieveBound:
                    bits[j] = False
                    j += 2 * i + 1
        yield 2
        for i in range(1, sieveBound+1):
            if bits[i]:
                yield 2*i+1
