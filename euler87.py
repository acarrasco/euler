def primes_to(n):
	primes = [2]
	for i in xrange(3, n, 2):
		if all(i%p for p in primes):
			primes.append(i)
	return primes

s = lambda a, b, c: a*a + b*b*b + c*c*c*c

limit = 50000000
primes = primes_to(int(limit**0.5))
numbers = set()
for a in primes:
	if s(a, 2, 2) >= limit: break
	for b in primes:
		if s(a, b, 2) >= limit: break
		for c in primes:
			n = s(a, b, c)
			if n >= limit: break
			else: numbers.add(n)
print(len(numbers))
