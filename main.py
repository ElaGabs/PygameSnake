# https://github.com/ElaGabs/PygameSnake.gitimport pygame
import sys
import random
import consts

pygame.init()

class Snake(object):
    def __int__(self):
        self.length = 1
        self.positions = [((consts.SCREEN_WIDTH/2), (consts.SCREEN_LENGTH/2))]
        self.direction = random.choice([UP, DOWN, RIGHT, LEFT])
        self.color = CORAL

    def head_position(self):
        return self.positions[0] #where is the head pointing to

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.head_position()
        x, y = self.direction
        new = (((current[0] + x *)))




class Food(object):
    pass


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range (0, int(GRID_WIDTH)):
            if ((x+y) %2) == 0:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, BLUE, rect)
            else:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, BLUE2, rect)







#Variables
#lengths
WIDTH = 480 #consts written
HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH/GRID_SIZE
GRID_HEIGHT = HEIGHT/GRID_SIZE
#colors
BLUE = (152,245,255)
BLUE2 = (121,205,205)
CORAL = (240,128,128)
#directions
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)


#main game loop
def main():
    clock= pygame.time.Clock()
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH), 0, 32)

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
