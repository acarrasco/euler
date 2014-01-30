from collections import defaultdict

lengths = defaultdict(int)
triangles = set()


def generate_triplet(m, n):
        return sorted((m*m - n*n, 2*m*n, m*m + n*n))

for m in range(2, 1200):
        for n in range(1, m):
                ka, kb, kc = a, b, c = generate_triplet(m, n)
                l = a+b+c
                k = 1
                while l*k <= 1500000:
                        triangles.add((ka,kb,kc))
                        k += 1
                        ka = k*a
                        kb = k*b
                        kc = k*c
for t in triangles:
        lengths[sum(t)] += 1

print sum(n == 1 for n in lengths.itervalues())
