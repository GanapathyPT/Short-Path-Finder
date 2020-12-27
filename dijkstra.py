import pygame
from helper import draw_path

def get_min_distance(distance, visited):
	minimum = next(iter(distance))

	for item in distance:
		if distance[item] < distance[minimum] and not visited[item]:
			minimum = item

	return minimum

def find_shortest_path(board):
	grid = board.grid
	start = board.start
	end = board.end

	visited = {col: False for row in grid for col in row}

	distance = {col: float("inf") for row in grid for col in row}
	distance[start] = 0

	from_list = {}

	while any(visited):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		current = get_min_distance(distance, visited)

		if current == end:
			draw_path(from_list, start, end)
			return

		for neighbour in current.get_neighbours(grid):
			temp_dist = distance[current] + 1
			if temp_dist < distance[neighbour]:
				distance[neighbour] = temp_dist
			
				from_list[neighbour] = current

		current.set_visited()
		current.draw()
		start.set_start()
		start.draw()
		pygame.display.update()
		visited[current] = True

