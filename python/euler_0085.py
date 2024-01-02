sqrt = lambda x: x**0.5
#this is the non integer exact solution to the problem, given one side
def solve(m):
    return (sqrt(m**4+2*m**3+32000001*m**2+32000000*m)-m**2-m)/(2*m**2+2*m)

def count_rectangles(n, m):
	return n * (n+1) * m * (m+1) // 4

def plausible_solutions():
    for m in range(1, int(solve(1))//2):
        n = int(solve(m))
        yield n, m
        yield n+1, m

TARGET = 2000000
def difference(sides):
    n, m = sides
    return abs(TARGET - count_rectangles(n, m))

n, m = min(plausible_solutions(), key=difference)
print(n * m)