from copy import deepcopy

operations = open('input.txt', 'r').read().split('\n')

width = 50
height = 6

def pretty_print_screen(screen_array):
	for j in range(len(screen_array)):
		print(*screen_array[j])
	print("END")

screen = [['.' for x in range(width)] for y in range(height)]

for op in operations:
	print(op)
	if op.startswith("rect"):
		temp = op.split(' ')[1].split('x')
		a = int(temp[0])
		b = int(temp[1])

		for j in range(b):
			for i in range(a):
				screen[j][i] = '#'
	elif op.startswith("rotate"):
		temp = op.split(' ')
		index = int(temp[2].split('=')[1])
		shift = int(temp[4])
		copy = deepcopy(screen)
		if temp[1]=="column":
			for row in range(height):
				screen[(row+shift)%height][index] = copy[row][index]
		elif temp[1]=="row":
			for col in range(width):
				 screen[index][(col+shift)%width] = copy[index][col]


pretty_print_screen(screen)

# Count lit pixel
count = 0
for j in range(height):
	for i in range(width):
		if (screen[j][i]=='#'):
			count += 1

print(count)


