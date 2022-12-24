import pygame
import random

# Initialize pygame
pygame.init()

# Set window size and title
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake')

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)

# Snake class


class Snake:
    def __init__(self):
        self.body = [pygame.Rect(100, 100, 10, 10), pygame.Rect(
            90, 100, 10, 10), pygame.Rect(80, 100, 10, 10)]
        self.direction = pygame.K_RIGHT

# Food class


class Food:
    def __init__(self):
        self.position = pygame.Rect(random.randint(
            0, 39) * 10, random.randint(0, 39) * 10, 10, 10)


# Create snake and food
snake = Snake()
food = Food()

# Main game loop
while True:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = pygame.K_UP
            if event.key == pygame.K_DOWN:
                snake.direction = pygame.K_DOWN
            if event.key == pygame.K_LEFT:
                snake.direction = pygame.K_LEFT
            if event.key == pygame.K_RIGHT:
                snake.direction = pygame.K_RIGHT

    # Update snake position
    if snake.direction == pygame.K_UP:
        snake.body.insert(0, pygame.Rect(
            snake.body[0].x, snake.body[0].y - 10, 10, 10))
    if snake.direction == pygame.K_DOWN:
        snake.body.insert(0, pygame.Rect(
            snake.body[0].x, snake.body[0].y + 10, 10, 10))
    if snake.direction == pygame.K_LEFT:
        snake.body.insert(0, pygame.Rect(
            snake.body[0].x - 10, snake.body[0].y, 10, 10))
    if snake.direction == pygame.K_RIGHT:
        snake.body.insert(0, pygame.Rect(
            snake.body[0].x + 10, snake.body[0].y, 10, 10))
    snake.body.pop()

    # Check if snake has collided with food
    if snake.body[0].colliderect(food.position):
        food.position = pygame.Rect(random.randint(
            0, 39) * 10, random.randint(0, 39) * 10, 10, 10)
        snake.body.append(pygame.Rect(
            snake.body[-1].x, snake.body[-1].y, 10, 10))

    # Draw game elements
    window.fill(BLACK)
    for segment in snake.body:
        pygame.draw.rect(window, WHITE, segment)
    pygame.draw.rect(window, GREEN, food.position)
    pygame.display.update()

    # Delay
    pygame.time.delay(100)
