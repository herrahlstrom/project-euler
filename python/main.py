"""
Generic solutions for Project eurler
https://projecteuler.net
"""

#pylint:disable=C0103,C0111,W0622

from eulerutils import Prime, Stopwatch

def get_answer():
    max = 99#9999

    primer = Prime(max)
    primes = primer.get_primes(max)
    primesums = len(primes) * [0]
    result_sum = 0
    result_length = 0

    primesums[0] = primes[0]
    for i in range(1, len(primes)):
        primesums[i] = primesums[i-1] + primes[i]

    for start in range(0, len(primes)):
        for end in range(len(primes)-1, start, -1):
            ps = primesums[end] - primesums[start]
            pslen = end - start + 1
            if ps > max:
                break
            if not ps in primes:
                break
            if pslen < result_length:
                break
            print(start, end)
            print(ps, pslen)
            for p in range(start, end+1):
                print(p, primes[p], primesums[i])
            result_length = pslen
            result_sum = ps
            break
    return result_sum

if __name__ == "__main__":
    print("Answer: {0}".format(get_answer()))
