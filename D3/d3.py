import re

# Read input
triangles = list(map(lambda s: re.sub(' +', ' ', s).strip().split(' '), open('input.txt', 'r').read().split('\n')))
valid_triangle_count = 0

for i in range(0, len(triangles), 3):
	for j in range(3):
		a = int(triangles[i][j])
		b = int(triangles[i+1][j])
		c = int(triangles[i+2][j])

		if (a+b > c) and (a+c > b) and (b+c > a):
			valid_triangle_count = valid_triangle_count + 1

print(valid_triangle_count)