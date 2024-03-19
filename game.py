import pygame

from direction import Direction
from game_state import GameState

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT_SIZE = 20

CUBE_SIZE = 25
CUBES_NUM = 20
WIDTH = CUBES_NUM * CUBE_SIZE
screen = pygame.display.set_mode((WIDTH, WIDTH))


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


def draw_score(score):
    font = pygame.font.SysFont("arial", FONT_SIZE)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))


def fill_bg():
    screen.fill(WHITE)


def show_game_over_screen(score):
    screen.fill(BLACK)

    font_game_over = pygame.font.SysFont("arial", 48)
    text_game_over = font_game_over.render("Game Over", True, RED)
    text_rect_game_over = text_game_over.get_rect(center=(WIDTH / 2, WIDTH / 3))

    font_score = pygame.font.SysFont("arial", 30)
    text_score = font_score.render(f"Your score: {score}", True, WHITE)
    test_rect_score = text_score.get_rect(center=(WIDTH / 2, WIDTH / 2))

    font_control = pygame.font.SysFont("arial", 15)
    text_control = font_control.render("(ENTER) to Return "
                                       "(ESCAPE) to Quit", True, WHITE)
    text_rect_control = text_control.get_rect(center=(WIDTH / 2, (WIDTH / 3) * 2))

    screen.blit(text_game_over, text_rect_game_over)
    screen.blit(text_score, test_rect_score)
    screen.blit(text_control, text_rect_control)

    pygame.display.flip()


def draw(snake, food, score):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    draw_score(score)
    pygame.display.update()


state = GameState(
    snake=None,
    direction=None,
    food=None,
    field_size=CUBES_NUM
)
state.set_initial_position()

clock = pygame.time.Clock()

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                state.turn(Direction.LEFT)
            if keys[pygame.K_RIGHT]:
                state.turn(Direction.RIGHT)
            if keys[pygame.K_UP]:
                state.turn(Direction.UP)
            if keys[pygame.K_DOWN]:
                state.turn(Direction.DOWN)
            if keys[pygame.K_RETURN]:
                state.set_initial_position()
                state.game_over = False
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()


    if state.game_over is True:
        show_game_over_screen(state.score)
    else:
        state.step()
        draw(state.snake, state.food, state.score)
