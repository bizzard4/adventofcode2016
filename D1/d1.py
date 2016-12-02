from enum import Enum

class Direction(Enum):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

def update_direction(current_direction, left_or_right):
	if (left_or_right == 'L'):
		return Direction((current_direction.value-1)%4)
	else:
		return Direction((current_direction.value+1)%4)

def update_position(current_postion, direction, translation):
	if (direction == Direction.NORTH):
		return (current_postion[0], current_postion[1]+translation)
	elif (direction == Direction.EAST):
		return (current_postion[0]+translation, current_postion[1])
	elif (direction == Direction.SOUTH):
		return (current_postion[0], current_postion[1]-translation)
	elif (direction == Direction.WEST):
		return (current_postion[0]-translation, current_postion[1])


# Read input
op = list(map(lambda s: s.replace(',',''), open('input_t4.txt', 'r').read().split(' ')))

# Initialize state
position = (0, 0) # x, y
direction = Direction.NORTH
visited_position = set()
visited_position.add((0,0))

for o in op:
	direction = update_direction(direction, o[0])
	position = update_position(position, direction, int(o[1:]))

	if (position in visited_position): # We been there 2 time
		print("We been there!")
		print(sorted(visited_position))
		break;
	else:
		visited_position.add(position);

	print("Now at " + str(position) + " facing " + str(direction))

print("Final direction " + str(direction))
print("Final position " + str(position))





