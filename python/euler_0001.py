import math

def sum_multiples(n, upto):
	m = math.ceil(1.0 * upto / n)
	return n * (m * m + 1) / 2

print(sum_multiples(3, 1000) + sum_multiples(5, 1000) - sum_multiples(15, 1000))
# print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 ==0))