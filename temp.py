import pygame


WIDTH = 480
HEIGHT = 480
BLUE = (152, 245, 255)
BLUE2 = (121, 205, 205)
CORAL = (240, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRID_SIZE = 20
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
font = pygame.font.Font('freesansbold.ttf', 30)


length = 1
positions = [((WIDTH / 2), (HEIGHT / 2))]
direction = random.choice([UP, DOWN, LEFT, RIGHT])
color = CORAL


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
    new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
    if len(self.positions) > 2 and new in self.positions[2:]:
        self.reset()
    else:
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()


def reset(self):
    self.length = 1
    self.positions = [((WIDTH / 2), (HEIGHT / 2))]
    self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    score = 0


def draw(self, surface):
    for p in self.positions:
        r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLUE2, r, 1)


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
            elif event.key == pygame.K_LEFT:
                self.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                self.turn(RIGHT)


