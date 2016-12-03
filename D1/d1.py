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

def check_if_visited(position, visited):
	if (position in visited):
		print("FOUND AT " + str(position))
		return True
	return False

def update_position(current_postion, direction, translation, visited):
	if (direction == Direction.NORTH):
		for i in range(translation):
			current_postion = (current_postion[0], current_postion[1]+1)
			if (check_if_visited(current_postion, visited)):
				return None
			visited.add(current_postion)
	elif (direction == Direction.EAST):
		for i in range(translation):
			current_postion = (current_postion[0]+1, current_postion[1])
			if (check_if_visited(current_postion, visited)):
				return None
			visited.add(current_postion)
	elif (direction == Direction.SOUTH):
		for i in range(translation):
			current_postion = (current_postion[0], current_postion[1]-1)
			if (check_if_visited(current_postion, visited)):
				return None
			visited.add(current_postion)
	elif (direction == Direction.WEST):
		for i in range(translation):
			current_postion = (current_postion[0]-1, current_postion[1])
			if (check_if_visited(current_postion, visited)):
				return None
			visited.add(current_postion)

	return current_postion


# Read input
op = list(map(lambda s: s.replace(',',''), open('input.txt', 'r').read().split(' ')))

# Initialize state
position = (0, 0) # x, y
direction = Direction.NORTH
visited_position = set()
visited_position.add((0,0))

for o in op:
	old_position = position
	direction = update_direction(direction, o[0])
	position = update_position(position, direction, int(o[1:]), visited_position)
	if (position is None):
		break

	print("Now at " + str(position) + " facing " + str(direction))

print("Final direction " + str(direction))
print("Final position " + str(position))





