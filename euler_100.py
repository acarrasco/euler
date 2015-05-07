import itertools

def diophantine_pairs(n):
	if n == 0:
		return 1
	elif n == 1:
		return 3
	return 6 * diophantine_pairs(n-1) - diophantine_pairs(n-2) - 2 

def generate_solutions():
	return itertools.imap(diophantine_pairs, itertools.count())

def total(blues):
	return (blues * (blues-1) * 2)**0.5

if __name__ == '__main__':
	print next(itertools.ifilter(lambda x: total(x)> 10**12, generate_solutions()))