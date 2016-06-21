
def isrightangle(v1, v2, v3):
	if v1 < 1 or v2 < 1 or v3 < 1: return False
	if v3 > v1 and v3 > v2: return (v1**2 + v2**2) == (v3**2)
	if v2 > v1 and v2 > v3: return (v1**2 + v3**2) == (v2**2)
	if v1 > v2 and v1 > v3: return (v3**2 + v2**2) == (v1**2)
	return False

def solutions(p):
	c = 0
	# v2 < v1 < v3
	for v1 in range(1,p//2):
		for v2 in range(1,v1+1):
			v3 = p - v1 - v2
			if v3 < v1: continue
			if isrightangle(v1, v2, v3):
				c += 1
	return c

highest = 0
highest_p = 0
	
# 3,4,5 is the smallest triangle

for p in range(12, 1000):
	c = solutions(p)
	if c > highest:
		print(p, c)
		highest = c
		highest_p = p

print(highest_p, highest)
