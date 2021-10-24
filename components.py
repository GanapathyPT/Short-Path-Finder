import pygame
from constants import BLUE, BLACK, GREEN, GREY, RED, ROWS, WHITE, WIDTH
from helper import *


class Item():
    ITEM_WIDTH = WIDTH // ROWS

    def __init__(self, screen, row, col):
        self.screen = screen
        self.row = row
        self.col = col
        self.color = WHITE
        self.neighbours = []

        self.x = self.row * self.ITEM_WIDTH
        self.y = self.col * self.ITEM_WIDTH

    def is_wall(self):
        return self.color == BLACK

    def set_start(self):
        self.color = GREEN

    def set_end(self):
        self.color = RED

    def set_wall(self):
        self.color = BLACK

    def set_visited(self):
        self.color = BLUE

    def set_path(self):
        self.color = GREY

    def get_neighbours(self, grid):
        neighbours = []

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            neighbours.append(grid[self.row - 1][self.col])

        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_wall():
            neighbours.append(grid[self.row + 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            neighbours.append(grid[self.row][self.col - 1])

        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].is_wall():
            neighbours.append(grid[self.row][self.col + 1])

        return neighbours

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x, self.y, self.ITEM_WIDTH, self.ITEM_WIDTH)
        )

    def get_pos(self):
        return self.x, self.y

    def __hash__(self):
        return self.x + self.y

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __str__(self):
        return f"{self.row}, {self.col}"


class Board():
    def __init__(self, screen):
        self.screen = screen
        self.grid = generate_grid(screen, ROWS, ROWS, Item)
        self.start = None
        self.end = None

    def _draw_lines(self):
        for row in self.grid:
            for col in row:
                x, y = col.get_pos()
                pygame.draw.rect(
                    self.screen,
                    BLACK,
                    pygame.Rect(x, y, col.ITEM_WIDTH, col.ITEM_WIDTH),
                    1
                )
        pygame.display.flip()

    def draw(self):
        for row in self.grid:
            for col in row:
                col.draw()

        self._draw_lines()
        pygame.display.update()
