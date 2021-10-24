from queue import PriorityQueue
from helper import draw_path
import pygame


def heuristic(pos1, pos2):
    # Manhattan Distance
    return abs(pos1.row - pos2.row) + abs(pos2.col - pos1.col)


def a_star(game):
    grid = game.grid
    start = game.start
    end = game.end

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    closed_set = [start]

    g_scores = {item: float("inf") for row in grid for item in row}
    g_scores[start] = 0

    f_score = {item: float("inf") for row in grid for item in row}
    f_score[start] = heuristic(start, end)

    from_list = {}

    while not open_set.empty():
        current = open_set.get()[2]
        closed_set.remove(current)

        if current == end:
            draw_path(from_list, start, end)
            return

        for neighbour in current.get_neighbours(grid):
            temp_g_score = g_scores[current] + 1

            if temp_g_score < g_scores[neighbour]:
                from_list[neighbour] = current

                g_scores[neighbour] = temp_g_score
                h_score = heuristic(neighbour, end)
                f_score = temp_g_score + h_score

                current.set_visited()
                current.draw()
                start.set_start()
                start.draw()
                pygame.display.update()

                if neighbour not in closed_set:
                    count += 1
                    open_set.put((f_score, count, neighbour))
                    closed_set.append(neighbour)
