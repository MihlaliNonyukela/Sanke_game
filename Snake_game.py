import pygame
import time
import random

pygame.init()

width = 600
height = 400

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Snake and food block size
block_size = 20
snake_speed = 15

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25)

def message(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3 + y_offset])

def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_body = []
    length_of_snake = 1

    # Random food position
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Boundary collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Collision with itself
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for part in snake_body:
            pygame.draw.rect(screen, green, [part[0], part[1], block_size, block_size])

        # Score
        score = length_of_snake - 1
        text = font.render(f"Score: {score}", True, white)
        screen.blit(text, [10, 10])

        pygame.display.update()

        # Eat food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
