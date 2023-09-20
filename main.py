import pygame
import sys
import random
pygame.init()

class Snake(object):
    def __int__(self):
        self.length = 1
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, RIGHT, LEFT])
        self.color = CORAL

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.get_head_position()
        x, y = self.direction
        new = (((current[0] + (x * GRID_SIZE)) % WIDTH), ((current[1] + (y * GRID_SIZE)) % HEIGHT))
        #collision
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()

        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, RIGHT, LEFT])
        score = 0

    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, BLUE2, rect, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)


class Food(object):
    def __int__(self):
        self.position = (0, 0)
        self. color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRID_SIZE), (random.randint(0, GRID_WIDTH-1)*GRID_SIZE)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)



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
WIDTH = 480
HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH/GRID_SIZE
GRID_HEIGHT = HEIGHT/GRID_SIZE
#colors
BLUE = (152,245,255)
BLUE2 = (121,205,205)
CORAL = (240,128,128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#directions
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
#fonts
font = pygame.font.Font("freesansbold.ttf", 30)



#main game loop
def main():
    pygame.init()
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
        snake.handle_keys()
        draw_grid(surface)
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = font.render("Score: {0}".format(score), True, BLACK)
        screen.blit(text, (5, 10))


        pygame.display.update()

main()
