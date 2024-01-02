import itertools

def diophantine_pairs(n):
	if n == 0:
		return 1
	elif n == 1:
		return 3
	return 6 * diophantine_pairs(n-1) - diophantine_pairs(n-2) - 2 

def generate_solutions():
	for i in itertools.count():
		yield diophantine_pairs(i)

def total(blues):
	return (blues * (blues-1) * 2)**0.5

print(next(filter(lambda x: total(x)> 10**12, generate_solutions())))