import pygame

from game_state import GameState

pygame.init()
pygame.display.set_caption("Snake Game")

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN_DART = (95, 50, 38)
GREEN_2_DART = (18, 147, 40)

CUBE_SIZE = 30
CUBES_NUM = 20
WIDTH = CUBES_NUM * CUBE_SIZE
screen = pygame.display.set_mode((WIDTH, WIDTH))


state = GameState(
    snake=None,
    direction=None,
    food=None,
    field_size=CUBES_NUM
)