import pygame

from game_variables import screen, CUBE_SIZE, FONT_SIZE, GREEN, BLUE, BLACK, WHITE


def draw_snake_part(pos):
    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)


def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)


def draw_food(pos):
    radius = float(CUBE_SIZE) / 2
    position = (pos.x * CUBE_SIZE + radius,
                pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, BLUE, position, radius)


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