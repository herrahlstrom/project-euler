from prime import Prime

def get_answer():
    p = Prime()
    in_row = 0
    value = 2 * 3 * 5 * 7
    while(in_row < 4):
        c = 0
        v = 0
        # This assume the prime factors is in order
        for pf in p.get_prime_factors(value):
            if pf != v:
                c +=1
                v = pf
        if c == 4:
            in_row += 1
            print(value, in_row)
        else:
            in_row = 0
        value += 1
    return value - in_row

def main():
    print("Answer: {0}".format(get_answer()))

if __name__ == "__main__":
	main();
