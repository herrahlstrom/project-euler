

def ispandigital(value):
	if value < 123456789: return False
	if value > 987654321: return False
	s = str(value)
	if "0" in s: return False
	return len(s) == 9 and (len(set(s)) == 9)

highest = 0

d = 1
while(d < 500000000):
	for n in range(2,9):
		s = ""
		i = 1
		while i <= n:
			s += str(d*i)
			i += 1
		if len(s) != 9:
			continue
		val = int(s)
		if not ispandigital(val):
			continue
		if val > highest:
			highest = val
		print(d, n, val)
	d += 1