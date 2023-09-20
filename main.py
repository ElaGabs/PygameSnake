import pygame
import sys
import random
pygame.init()

class Snake(object):
    pass


class Food(object):
    pass


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range (0, int(GRID_WIDTH)):
            if ((x+y) %2) == 0:
                rect = pygame.Rect()





#Variables
WIDTH = 480
HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH/GRID_SIZE
GRID_HEIGHT = HEIGHT/GRID_SIZE

#main game loop
def main():
    clock= pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    draw_grid(surface)

    snake = Snake()
    food = Food()

    score = 0
    while True:
        clock.tick(10)
        #snake + food sub-functions
        draw_grid(surface)

        pygame.display.update()

main()
