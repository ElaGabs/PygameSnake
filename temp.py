import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # screen
pygame.display.set_caption("Snake Game") #screen

# Initialize the Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)] # snake
snake_direction = (0, -1)  # Start moving up # snake

# Initialize the food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)) # food


def handle_user_events(snake_direction):
    keys = pygame.key.get_pressed()
    new_direction = snake_direction

    # Check for arrow key input to change direction
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        new_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        new_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        new_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        new_direction = (1, 0)

    snake_direction = new_direction

    return snake_direction


# Game loop
running = True # main ⬇️
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys = pygame.key.get_pressed()
    # new_direction = snake_direction
    #
    # # Check for arrow key input to change direction
    # if keys[pygame.K_UP] and snake_direction != (0, 1):
    #     new_direction = (0, -1)
    # elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
    #     new_direction = (0, 1)
    # elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
    #     new_direction = (-1, 0)
    # elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
    #     new_direction = (1, 0)

    # Update snake direction
    # snake_direction = new_direction
    snake_direction = handle_user_events(snake_direction)

    # Move the snake
    head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, head)

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for collisions with the walls
    # if (
    #     snake[0][0] < 0
    #     or snake[0][0] >= GRID_WIDTH
    #     or snake[0][1] < 0
    #     or snake[0][1] >= GRID_HEIGHT
    # ):
    #     running = False

    # Check for collisions with the snake's own body
    if snake[0] in snake[1:]:
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Draw the food
    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    pygame.display.flip()

# # Quit pygame
# pygame.quit()


