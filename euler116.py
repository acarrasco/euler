import math

def p(a, b):
	res = math.factorial(a+b) // (math.factorial(a) * math.factorial(b))
	#print a, b, res
	return res

def ways_fixed_size(size, block_size):
	return sum(p(size-n*block_size, n) for n in range(1, size//block_size + 1))

def ways(size):
	return sum(ways_fixed_size(size, block_size) for block_size in (2, 3, 4))

print ways(5)
print ways(50)
