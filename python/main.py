from prime import Prime

def test_value(value, p):
    for n in range(value - 2, 1, -1):
        if not p.is_prime(n):
            continue
        m = 0
        while True:
            m+=1
            s = n + 2 * (m ** 2)
            if s > value:
                break
            if s == value:
                return True
    return False

def get_answer():
    p = Prime()
    
    i = 1
    while True:
        i+=2
        if p.is_prime(i):
            continue
        if test_value(i, p):
            continue
        return i

def main():
    print("Answer: {0}".format(get_answer()))

if __name__ == "__main__":
	main();
