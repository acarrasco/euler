sqrt = lambda x: x**0.5
#this is the non integer exact solution to the problem, given one side
calcn = lambda m:(sqrt(m**4+2*m**3+32000001*m**2+32000000*m)-m**2-m)/(2*m**2+2*m)

def rectangles(n,m):
	return n*(n+1)*m*(m+1)/4

def generate_plausible_solutions():
    for m in range(1,int(calcn(1))//2):
        n = int(calcn(m))
        yield n, m
        yield n+1, m

print min((abs(2000000-rectangles(n,m)), n*m) for n, m in generate_plausible_solutions())[1]
