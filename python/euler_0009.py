for a in range(1, 999):
	for b in range(a, 1000-a):
		c = 1000 - a - b
		if a*a + b*b == c*c:
			print(a*b*c)