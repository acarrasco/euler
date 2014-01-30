from itertools import count
from functools import wraps

primes = tuple(int(x) for line in open('10000primes.txt') for x in line.split())[:1000]

def memoize(f):
	cache = {}
	@wraps(f)
	def memoized(*args):
		res = cache.get(args)
		if res is None:
			res = f(*args)
			cache[args] = res
		return res
	return memoized

@memoize
def ways(n, p):
	if n == 0:
		return 1
	if n < 0 or p[0] > n:
		return 0
	else:
		return (ways(n - p[0], p) +
			ways(n, p[1:]))

def check(n):
	return ways(n, primes) > 5000

print next(n for n in count(2) if check(n))
