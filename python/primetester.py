class primetester:
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11]
        self.highestprime = 11

    def isprime(self, value):
        if self.highestprime < value:
            self.calcprimes(value)
        return value in self.primes

    # yield 2
    # i = 3
    # while True:
    # if self.isprime(i):
    # yield i
    # i += 2

    def calcprimes(self, until):
        i = self.highestprime
        while self.highestprime < until:
            i += 2
            match = False
            for j in self.primes:
                if i % j == 0:
                    match = True
                    break
            if not match:
                self.primes.append(i)
                self.highestprime = i
