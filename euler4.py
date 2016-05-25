def is_palindrome(n):
	digits = str(n)
	return digits == digits[::-1]

print max(n * m for n in range (100, 1000) for m in range (100, 1000) if is_palindrome(n * m))
