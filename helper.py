import pygame
from constants import *


def generate_grid(screen, rows, cols, Item):
    grid = []
    for row in range(rows):
        grid.append([])
        for col in range(cols):
            grid[row].append(Item(screen, row, col))

    return grid


def get_pos(x, y):
    return x // (WIDTH // ROWS), y // (WIDTH // ROWS)


def handle_mouse_event(board):
    grid = board.grid
    start = board.start
    end = board.end

    x, y = pygame.mouse.get_pos()
    row, col = get_pos(x, y)

    if not start:
        grid[row][col].set_start()
        board.start = grid[row][col]

    elif not end and grid[row][col] != start:
        grid[row][col].set_end()
        board.end = grid[row][col]

    elif grid[row][col] != start and grid[row][col] != end:
        grid[row][col].set_wall()


def draw_path(from_list, start, end):
    if end == start:
        return
    end.set_path()
    draw_path(from_list, start, from_list[end])
