



import pygame
import time
import random

pygame.init()

# Colors
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (0, 255, 0)

# Window dimensions
win_width = 800
win_height = 600

# Initialize window
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Advanced Snake Game")

# Font styles
font_style = pygame.font.SysFont("calibre", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# Game variables
snake_block = 10
snake_speed = 15
score = 0
food_x = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
snake_list = []
snake_length = 1
direction = 'RIGHT'

# Game functions
def user_score(score):
    number = score_font.render("Score: " + str(score), True, red)
    window.blit(number, [0, 0])

def game_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, blue, [x[0], x[1], snake_block, snake_block])

def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 6, win_height / 3])

def game_loop():
    global direction
    global score
    global snake_length
    global snake_list
    global food_x
    global food_y

    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_height / 2
    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close == True:
            window.fill(grey)
            message("You Lost! Press P to Play Again")
            user_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'UP'
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        game_snake(snake_block, snake_list)
        user_score(score)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            score += 1
            snake_length += 1
            food_x = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
