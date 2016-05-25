import itertools

def fibgen():
	a = 1
	b = 1
	while True:
		yield b
		a, b = b, a + b

print sum(x for x in itertools.takewhile(lambda x: x < 4000000, fibgen()) if x % 2 == 0)
