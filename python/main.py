import time


def get_triangle(n):
    return n * (n + 1) // 2
def get_pentagonal(n):
    return n * (3 * n - 1) // 2
def get_hexagonal(n):
    return n * (2 * n - 1)

def get_answer():
    t = (1, get_triangle(1))
    p = (1, get_pentagonal(1))
    h = (1, get_hexagonal(1))
    hits = 0    

    while True:
        if t[1] <= p[1] and t[1] <= h[1]:
            t = (t[0] + 1, get_triangle(t[0] + 1))
        elif p[1] <= t[1] and p[1] <= h[1]:
            p = (p[0] + 1, get_pentagonal(p[0] + 1))
        elif h[1] <= p[1] and h[1] <= t[1]:
            h = (h[0] + 1, get_hexagonal(h[0] + 1))
        else:
            raise Exception("Something is wrong with math!")
        if t[1] == p[1] and t[1] == h[1]:
            hits += 1
            if hits == 2:
                return t[1]

def main():
    start = time.time()
    answer = get_answer()
    end = time.time()
    print("Answer: {0}".format(answer))
    print("{0:.0f} ms".format((end-start)*1000))

if __name__ == "__main__":
	main();