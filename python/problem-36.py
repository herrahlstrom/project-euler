import time
from eulerutils import int2base

try:
	t1 = time.time()
	s = 0
	for i in range(1,999999,2):
		base10 = str(i)
		if base10 != base10[::-1]:
			continue
		base2 = int2base(i,2)
		if base2 != base2[::-1]:
			continue
		print("{0:>20}	{1:>6}".format(base2, base10))
		s += i
	t2 = time.time()
	
	print()
	print("Sum",s)
	print("Elapsed", t2-t1)

except Exception as e:
	for arg in e.args:
		print(arg)

input("Pause...")