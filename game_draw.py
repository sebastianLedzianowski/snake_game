import pygame

from game_variables import screen, CUBE_SIZE, FONT_SIZE, BLACK, WHITE, state


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
    font = pygame.font.SysFont("arial", FONT_SIZE)
    text = font.render(f"Hi {player_name} this is your score: {score}", True, BLACK)
    screen.blit(text, (10, 10))


def fill_bg():
    screen.fill(WHITE)


def draw(snake, food, player_name, score):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    draw_score(player_name, score)
    pygame.display.update()