import pygame
import sys
import random
import consts
import ImageEdit
import screen

pygame.init()


class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((consts.WIDTH / 2), (consts.HEIGHT / 2))]
        self.direction = random.choice([consts.UP, consts.DOWN, consts.LEFT, consts.RIGHT])
        self.color = consts.CORAL

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * consts.GRID_SIZE)) % consts.WIDTH), (cur[1] + (y * consts.GRID_SIZE)) % consts.HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((consts.WIDTH / 2), (consts.HEIGHT / 2))]
        self.direction = random.choice([consts.UP, consts.DOWN, consts.LEFT, consts.RIGHT])
        score = 0

    def draw(self, surface):
        # r = pygame.Rect((p[0], p[1]), (consts.GRID_SIZE, consts.GRID_SIZE))
        # pygame.draw.rect(surface, self.color, r)
        # pygame.draw.rect(surface, consts.BLUE2, r, 1)
        for p in self.positions:
            self.image = consts.CART_UP
            surface.blit(self.image, (p[0], p[1]))


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(consts.UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(consts.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(consts.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(consts.RIGHT)


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = ImageEdit.pick_rand_npc()
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, consts.GRID_WIDTH - 1) * consts.GRID_SIZE,
                         random.randint(0, consts.GRID_HEIGHT - 1) * consts.GRID_SIZE)
        self.color = ImageEdit.pick_rand_npc()

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (consts.GRID_SIZE, consts.GRID_SIZE))
        # pygame.draw.rect(surface, consts.CORAL, r)
        # pygame.draw.rect(surface, consts.BLUE2, r, 1)
        surface.blit(self.color, r)


def drawGrid(surface):
    for y in range(0, int(consts.GRID_HEIGHT)):
        for x in range(0, int(consts.GRID_WIDTH)):
            if ((x + y) % 2) == 0:
                r = pygame.Rect((x * consts.GRID_SIZE, y * consts.GRID_SIZE), (consts.GRID_SIZE, consts.GRID_SIZE))
                pygame.draw.rect(surface, consts.BLUE, r)
            else:
                rr = pygame.Rect((x * consts.GRID_SIZE, y * consts.GRID_SIZE), (consts.GRID_SIZE, consts.GRID_SIZE))
                pygame.draw.rect(surface, consts.BLUE, rr)




def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((consts.WIDTH, consts.HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    score = 0
    while True:
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = consts.font.render("Score {0}".format(score), True, consts.BLACK)
        screen.blit(text, (5, 10))
        pygame.display.update()


main()
