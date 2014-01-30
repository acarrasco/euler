import math
from itertools import ifilter, count

def find_blue_slow(total):
	d = total*(total-1)
	n = math.ceil((d // 2)**0.5)
	if n * (n-1) * 2 == d:
		return n, total
	else:
		return None

def solve_slow():
	print next(ifilter(None, (find_blue(x) for x in count(10**12))))

def has_fifty_percent(blues):
	denominator = blues * (blues-1) * 2
	total = int(denominator ** 0.5)
	return total * (total + 1) == denominator

def solve_fast(total):
	d = total * (total - 1)
	first_guess = int(math.ceil((d // 2)**0.5))
	print next(x for x in count(first_guess) if has_fifty_percent(x))
	

if __name__ == '__main__':
	solve_fast(10**12 + 1)
