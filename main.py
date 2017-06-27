"""
Generic solutions for Project eurler
https://projecteuler.net
"""

#pylint:disable=C0103,C0111,W0622,C0303

from eulerutils import Prime,Stopwatch

def get_answer():
    max = 999999

    primer = Prime(max)

    primes = primer.get_primes(max)
    primesums = len(primes) * [0]
    result_sum = 0
    result_length = 0

    primesums[0] = primes[0]
    for i in range(1, len(primes)):
        primesums[i] = primesums[i-1] + primes[i]
 
    # Predict start value not to be greater then 10, and it worked (solution started at 7)
    for start in range(0, 10):
        for end in range(len(primes)-1, start, -1):
            c_len = end - start + 1
            if c_len <= result_length:
                break
            
            c_sum = primesums[end]
            if start > 0:
                c_sum -= primesums[start-1]
            
            if c_sum <= max and c_sum in primes:
                result_length = c_len
                result_sum = c_sum
                break

    return result_sum

if __name__ == "__main__":
    sw = Stopwatch.start_new()
    print("Answer: {0}".format(get_answer()))
    print("Elapsed time: {0:.2f} s".format(sw.get_elapsed()))
