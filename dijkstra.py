import pygame
from helper import draw_path


def get_vertex_with_min_distance(vertices, distance_dict):
    min_dist_vertex = vertices[0]

    for vertex in vertices:
        if distance_dict[vertex] < distance_dict[min_dist_vertex]:
            min_dist_vertex = vertex

    return min_dist_vertex


def dijkstra(board):
    grid = board.grid
    start = board.start
    end = board.end

    vertex_set = []
    distance_set = {}
    prev_set = {}

    for row in grid:
        for col in row:
            distance_set[col] = float("inf")
            prev_set[col] = None
            vertex_set.append(col)

    distance_set[start] = 0

    while len(vertex_set) > 0:
        current = get_vertex_with_min_distance(vertex_set, distance_set)

        if current == end and distance_set[current] != float('inf'):
            draw_path(prev_set, start, end)
            return

        vertex_set.remove(current)

        for neighbour in current.get_neighbours(grid):
            if neighbour in vertex_set:
                temp_dist = distance_set[current] + 1
                if temp_dist < distance_set[neighbour]:
                    distance_set[neighbour] = temp_dist
                    prev_set[neighbour] = current

                    current.set_visited()
                    current.draw()
                    start.set_start()
                    start.draw()
                    pygame.display.update()
