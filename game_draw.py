import pygame
import random

from direction import Direction
from game_variables import screen, CUBE_SIZE, BLACK, WHITE, state, WIDTH


def draw_snake_part(image, pos, angle):
    image = pygame.transform.scale(image, (CUBE_SIZE, CUBE_SIZE))
    image = pygame.transform.rotate(image, angle)

    position = (pos.x * CUBE_SIZE, pos.y * CUBE_SIZE)

    screen.blit(image, position)


def draw_snake(snake):
    for i, part in enumerate(snake):
        angle = 0
        if i == len(snake) - 1:
            head_image = pygame.image.load('static/snake_head.png')
            angle = state.direction
            draw_snake_part(head_image, part, angle)
        elif i == 0:
            tail_image = pygame.image.load('static/snake_tail.png')
            prev_part = snake[i + 1]
            if prev_part.x < part.x:
                angle = Direction.LEFT
            elif prev_part.x > part.x:
                angle = Direction.RIGHT
            elif prev_part.y < part.y:
                angle = Direction.UP
            elif prev_part.y > part.y:
                angle = Direction.DOWN
            draw_snake_part(tail_image, part, angle)
        else:
            body_image = pygame.image.load('static/snake_body.png')
            draw_snake_part(body_image, part, angle)


def draw_food(pos):
    food_image = pygame.image.load('static/food.png')
    food_image = pygame.transform.scale(food_image, (CUBE_SIZE, CUBE_SIZE))

    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE)
    screen.blit(food_image, position)


def draw_score(player_name, score):
    font = pygame.font.SysFont("arial", CUBE_SIZE)
    text = font.render(f"Hi {player_name} this is your score: {score}", True, BLACK)
    screen.blit(text, (10, 10))


def fill_bg():
    background = pygame.Surface((WIDTH, WIDTH))
    background.fill(WHITE)

    dart_1 = pygame.image.load('static/dart_1.png')
    dart_1 = pygame.transform.scale(dart_1, (CUBE_SIZE, CUBE_SIZE))

    dart_2 = pygame.image.load('static/dart_2.png')
    dart_2 = pygame.transform.scale(dart_2, (CUBE_SIZE, CUBE_SIZE))

    for row in range(CUBE_SIZE):
        for col in range(CUBE_SIZE):
            dart = dart_1 if random.random() < 0.75 else dart_2
            background.blit(dart, (col * CUBE_SIZE, row * CUBE_SIZE))

    return background

def draw(snake, food, player_name, score):
    draw_snake(snake)
    draw_food(food)
    draw_score(player_name, score)
    pygame.display.update()