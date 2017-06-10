from prime import Prime

def get_answer():
    p = Prime()
    
    p1 = Prime.get_primes(5)
    p2 = (Prime.get_primes(5))
    p3 = [Prime.get_primes(5)]
    p4 = list(Prime.get_primes(5))

    t = Prime.get_prime_factors(17);
    return 5

def main():
    print("Answer: {0}".format(get_answer()))

if __name__ == "__main__":
	main();
