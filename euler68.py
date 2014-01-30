import itertools
def check(p):
	return (p[0] + p[1] + p[3] ==
		p[2] + p[3] + p[5] ==
		p[4] + p[5] + p[7] ==
		p[6] + p[7] + p[9] ==
		p[8] + p[9] + p[1])

def normalize(p):
	lowest = min(p[i*2] for i in range(0,5))
	lowestIdx = p.index(lowest)
	return "".join("".join(map(str,(p[i%10], p[(i+1)%10], p[(i+3)%10]))) for i in range(lowestIdx, lowestIdx+9, 2))

print max(normalize((10,)+p) for p in itertools.permutations(range(1,10)) if check((10,)+p))
