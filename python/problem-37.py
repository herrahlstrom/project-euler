#from eulerutils import isprime
from primetester import primetester
from time import sleep

pt = primetester()

def isPrimeFromLeft(value):
	#print("isPrimeFromLeft",value)
	if not pt.isprime(value):
		return False
	if value < 10:
		return True
	elif value < 100:
		return isPrimeFromLeft(value % 10)
	elif value < 1000:
		return isPrimeFromLeft(value % 100)
	elif value < 10000:
		return isPrimeFromLeft(value % 1000)
	elif value < 100000:
		return isPrimeFromLeft(value % 10000)
	elif value < 1000000:
		return isPrimeFromLeft(value % 100000)
	elif value < 10000000:
		return isPrimeFromLeft(value % 1000000)
	else:
		raise Exception("To high")

def isPrimeFromRight(value):
	#print("isPrimeFromRight",value)
	if not pt.isprime(value):
		return False
	if value < 10:
		return True
	else:
		return isPrimeFromRight(value // 10)

s = 0
c = 0
i = 11
a = 0
for i in getprimes(1000000):
	#sleep(1)
	a += 1
	if a > 1000:
		print(i)
		a = 0
	if i < 10: continue
	if not isPrimeFromLeft(i): continue
	if not isPrimeFromRight(i//10): continue
	print("ja", i)
	s += i
	c += 1
	if c >= 11: break
	
print("result", s)
input("Pause")