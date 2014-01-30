from collections import Counter
from math import factorial
from operator import mul

def prod(seq): return reduce(mul, seq)

def permutations(repeated_elements):
	total = factorial(sum(repeated_elements))
	equivalent = prod(map(factorial, repeated_elements))
	return total // equivalent

def block_choices(remaining_size, available_blocks, used_blocks):
	if remaining_size == 0:
		yield Counter(used_blocks).values()
	elif remaining_size > 0 and available_blocks:
		h, t = available_blocks[0], available_blocks[1:]
		for choice in block_choices(remaining_size - h, available_blocks, used_blocks+(h,)):
			yield choice
		for choice in block_choices(remaining_size, t, used_blocks):
			yield choice

def ways(size):
	blocks = (1, 2, 3, 4)
	return sum(map(permutations, block_choices(size, blocks, ())))

print ways(5)
print ways(50)
