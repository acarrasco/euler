from itertools import *

cache = [0]

def is_pythagorean(a, b):
	c2 = a**2 + b**2
	return (int(c2**0.5))**2 == c2

def summations(i, n):
	if i <= n:
		return i // 2
	else:
		return n - (i+1)//2 + 1

def solutions(m):
	if len(cache) > m:
		return cache[m]
	for n in range(len(cache), m+1):
		new_solutions = sum(is_pythagorean(n, i) * summations(i, n)
			for i in range(2, 2*(n+1)))
		cache.append(cache[n-1] + new_solutions)
	return cache[m]

print(next(m for m in count() if solutions(m) > 1000000))