MAX = 4000000

def seq():
	a = 1
	b = 1
	while b < MAX:
		if b % 2 == 0:
			yield b
		a, b = b, a + b

print(sum(seq()))