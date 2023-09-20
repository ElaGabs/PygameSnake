import pygame
pygame.init()

TRAIN_HEIGHT = 50
TRAIN_WIDTH = 50

NPC_HEIGHT = 50
NPC_WIDTH = 50

# screen
WIDTH = 480
HEIGHT = 480

BLUE = (152,245,255)
BLUE2 = (121,205,205)
CORAL = (240,128,128)
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

# NPC generate
npc1 = pygame.image.load("photos/LEGO_1.png")
npc1 = pygame.transform.scale(npc1, (NPC_HEIGHT, NPC_WIDTH))

npc2 = pygame.image.load("photos/LEGO_2.png")
npc2 = pygame.transform.scale(npc2, (NPC_HEIGHT, NPC_WIDTH))

npc3 = pygame.image.load("photos/LEGO_3.png")
npc3 = pygame.transform.scale(npc3, (NPC_HEIGHT, NPC_WIDTH))

npc4 = pygame.image.load("photos/LEGO_4.png")
npc4 = pygame.transform.scale(npc4, (NPC_HEIGHT, NPC_WIDTH))

npc5 = pygame.image.load("photos/LEGO_5.png")
npc5 = pygame.transform.scale(npc5, (NPC_HEIGHT, NPC_WIDTH))

npc6 = pygame.image.load("photos/LEGO_6.png")
npc6 = pygame.transform.scale(npc6, (NPC_HEIGHT, NPC_WIDTH))

npc7 = pygame.image.load("photos/LEGO_7.png")
npc7 = pygame.transform.scale(npc7, (NPC_HEIGHT, NPC_WIDTH))

npc8 = pygame.image.load("photos/LEGO_8.png")
npc8 = pygame.transform.scale(npc8, (NPC_HEIGHT, NPC_WIDTH))

npc9 = pygame.image.load("photos/LEGO_9.png")
npc9 = pygame.transform.scale(npc9, (NPC_HEIGHT, NPC_WIDTH))

npc10 = pygame.image.load("photos/LEGO_10.png")
npc10 = pygame.transform.scale(npc10, (NPC_HEIGHT, NPC_WIDTH))

npc11 = pygame.image.load("photos/LEGO_11.png")
npc11 = pygame.transform.scale(npc11, (NPC_HEIGHT, NPC_WIDTH))

npc12 = pygame.image.load("photos/LEGO_12.png")
npc12 = pygame.transform.scale(npc12, (NPC_HEIGHT, NPC_WIDTH))

npc13 = pygame.image.load("photos/LEGO_13.png")
npc13 = pygame.transform.scale(npc13, (NPC_HEIGHT, NPC_WIDTH))

npc14 = pygame.image.load("photos/LEGO_14.png")
npc14 = pygame.transform.scale(npc14, (NPC_HEIGHT, NPC_WIDTH))


# train
TRAIN = pygame.image.load("photos/train.png")
TRAIN = pygame.transform.scale(TRAIN, (TRAIN_HEIGHT, TRAIN_WIDTH))

TRAIN_CART = pygame.image.load("photos/train_cart.png")
TRAIN_CART = pygame.transform.scale(TRAIN_CART, (TRAIN_HEIGHT, TRAIN_WIDTH))



