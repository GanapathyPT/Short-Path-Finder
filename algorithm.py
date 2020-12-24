def get_min_distance(distance, unvisited):
	minimum = next(iter(distance))

	for item in distance:
		if distance[item] < distance[minimum] and not unvisited[item]:
			minimum = item

	return minimum

def draw_path(from_list, start, end):
	if end == start:
		return
	end.set_path()
	draw_path(from_list, start, from_list[end])


def find_shortest_path(board):
	grid = board.grid
	start = board.start
	end = board.end

	unvisited = {col: False for row in grid for col in row}

	distance = {col: float("inf") for row in grid for col in row}
	distance[start] = 0

	from_list = {}

	while any(unvisited):
		current = get_min_distance(distance, unvisited)

		if current == end:
			draw_path(from_list, start, end)
			return True

		for neighbour in current.get_neighbours(grid):
			temp_dist = distance[current] + 1
			if temp_dist < distance[neighbour]:
				distance[neighbour] = temp_dist
			
				from_list[neighbour] = current

		current.set_visited()
		unvisited[current] = True

	return False