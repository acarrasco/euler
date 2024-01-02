from itertools import count
from functools import cache

primes = tuple(int(x) for x in open('10000primes.txt').read().split()[:1000])

@cache
def ways_to_sum(n, numbers):
	if n == 0:
		return 1
	if n < 0 or numbers[0] > n:
		return 0
	else:
		return (
			ways_to_sum(n - numbers[0], numbers) +
			ways_to_sum(n, numbers[1:])
		)

def check(n):
	return ways_to_sum(n, primes) > 5000

print(next(n for n in count(2) if check(n)))