# Read input
op = open('input.txt', 'r').read().split('\n')

# Pad and current position
#pad = [[1, 2, 3],[4, 5, 6],[7, 8 ,9]]
pad = [['X', 'X', '1', 'X', 'X'],['X', '2', '3', '4', 'X'],['5', '6', '7', '8', '9'],['X', 'A', 'B', 'C', 'X'],['X', 'X', 'D', 'X', 'X']]
pos = (2,0)

# Final code
code = []

for instruction_set in op:
	for c in instruction_set:
		old_position = pos
		if (c == 'U'):
			if ((pos[0]-1)>=0):
				if (pad[pos[0]-1][pos[1]]!='X'):
					pos = (pos[0]-1, pos[1])
		elif(c=='D'):
			if ((pos[0]+1)<=4):
				if (pad[pos[0]+1][pos[1]]!='X'):
					pos = (pos[0]+1, pos[1])
		elif(c=='L'):
			if ((pos[1]-1)>=0):
				if (pad[pos[0]][pos[1]-1]!='X'):
					pos = (pos[0], pos[1]-1)
		elif(c=='R'):
			if ((pos[1]+1)<=4):
				if (pad[pos[0]][pos[1]+1]!='X'):
					pos = (pos[0], pos[1]+1)
	# End foor
	code.append(pad[pos[0]][pos[1]])


print(*code)
