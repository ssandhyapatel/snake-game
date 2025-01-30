import pygame
import random
import time

pygame.init()

# Colors
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Window dimensions
win_width = 800
win_height = 600

# Initialize window
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Advanced Snake Game")

# Font styles
font_style = pygame.font.SysFont("calibre", 26)
menu_font = pygame.font.SysFont("comicsansms", 50)
score_font = pygame.font.SysFont("comicsansms", 30)

# Initialize game variables
snake_block = 10
snake_speed = 15
score = 0
food_x = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
special_food = None
snake_list = []
snake_length = 1
direction = 'RIGHT'
obstacles = []
bounded = True


# Function for rendering text
def draw_text(text, font, color, surface, x, y, center=False):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


# Function for buttons
def draw_button(text, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))

    draw_text(text, font_style, black, window, x + w / 2, y + h / 2, center=True)


# Main menu
def main_menu():
    while True:
        window.fill(grey)
        draw_text("Snake Game", menu_font, blue, window, win_width / 2, win_height / 4, center=True)
        draw_button("Play", win_width / 2 - 75, win_height / 2 - 50, 150, 50, green, blue, game_loop)
        draw_button("Settings", win_width / 2 - 75, win_height / 2 + 20, 150, 50, green, blue, settings_menu)
        draw_button("Quit", win_width / 2 - 75, win_height / 2 + 90, 150, 50, red, black, quit_game)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()


# Settings menu
def settings_menu():
    global bounded, snake_speed
    while True:
        window.fill(white)
        draw_text("Settings", menu_font, blue, window, win_width / 2, win_height / 4, center=True)
        draw_text(f"Boundaries: {'On' if bounded else 'Off'}", font_style, black, window, win_width / 2, win_height / 2, center=True)
        draw_button("Toggle Boundaries", win_width / 2 - 120, win_height / 2 + 50, 240, 50, grey, green, toggle_boundaries)
        draw_button("Back", win_width / 2 - 75, win_height - 100, 150, 50, green, blue, main_menu)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()


# Toggle boundaries
def toggle_boundaries():
    global bounded
    bounded = not bounded


# Quit game
def quit_game():
    pygame.quit()
    quit()


# Game loop
def game_loop():
    global direction, score, snake_length, snake_list, food_x, food_y, special_food, obstacles, bounded, snake_speed

    x1 = win_width / 2
    y1 = win_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1
    score = 0
    level = 1
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                    x1_change = 0
                    y1_change = snake_block

        if bounded and (x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0):
            main_menu()
        elif not bounded:
            x1 %= win_width
            y1 %= win_height

        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        pygame.draw.rect(window, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                main_menu()

        for block in snake_list:
            pygame.draw.rect(window, blue, [block[0], block[1], snake_block, snake_block])

        draw_text(f"Score: {score}", font_style, white, window, 10, 10)

        if x1 == food_x and y1 == food_y:
            score += 1
            snake_length += 1
            food_x = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

        pygame.display.update()
        clock.tick(snake_speed)


# Start the game
main_menu()
