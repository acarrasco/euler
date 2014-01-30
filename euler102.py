def ntuples(lst, n):
    return zip(*[lst[i:]+lst[:i] for i in range(n)])

def x_product(a, b):
	x,y = a
	v,w = b
	return x*w-y*v

def parse(line):
	l = [int(i) for i in line.split(",")]
	return zip(l[0::2], l[1::2])

def minus(a, b):
	x,y = a
	v,w = b
	return (x-v, y-w)

def all_equal(seq):
	it = iter(seq)
	first = it.next()
	return all(i==first for i in it)

def inside_convex(poly, point):
	edges = (minus(a,b) for a,b in ntuples(poly,2))
	point_v = (minus(a,point) for a in poly)
	x_products = (x_product(a,b) for a,b in zip(point_v, edges))
	return all_equal(int(i/abs(i)) for i in x_products)

print(sum(inside_convex(parse(line), (0,0)) for line in file("triangles.txt")))

