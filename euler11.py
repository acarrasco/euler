import euler_common
import itertools

grid = [map(int, line.split()) for line in open("euler11_input.txt")]


adjacency = [(0, 1), (1, 0), (1, 1), (1, -1)]
def group((i, j), (di, dj)):
	return tuple(grid[i+di*n][j+dj*n] for n in range(4))

def in_bounds((i, j), (di, dj)):
	return 0 <= i + di * 3 < len(grid) and 0 <= j + dj * 3 < len(grid[i])

def all_groups():
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			for (di, dj) in adjacency:
				if in_bounds((i, j), (di, dj)):
					yield group((i, j), (di, dj))

print max(itertools.starmap(euler_common.prod, all_groups()))
