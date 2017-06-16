"""
Generic solutions for Project eurler
https://projecteuler.net
"""

from prime import Prime
from utils import ListUtil

def get_answer():
    """
    Calculate the answer for the current problem
    """

    ptester = Prime()
    lutil = ListUtil()

    for a in [x for x in ptester.get_primes(9999) if x >= 1000]:
        a_permutations = [int(x) for x in lutil.permute(str(a))]
        for delta in range(1, 9999):
            b = a + delta
            c = b + delta
            if a > 9999 or b > 9999:
                continue
            if not b in a_permutations or not c in a_permutations:
                continue
            if not ptester.is_prime(b) or not ptester.is_prime(c):
                continue
            if a == 1487 and b == 4817 and c == 8147:
                continue
            return "{0}{1}{2}".format(a, b, c)
    raise RuntimeError("Not found")

if __name__ == "__main__":
    print("Answer: {0}".format(get_answer()))
