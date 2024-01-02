def is_palindrome(n):
	digits = str(n)
	return digits == digits[::-1]

MIN = 100
MAX = 1000
def seq():
	for n in range(MIN, MAX):
		for m in range(n, MAX):
			yield n * m

print(max(filter(is_palindrome, seq())))