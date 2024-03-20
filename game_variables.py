import pygame

from game_state import GameState

pygame.init()

BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT_SIZE = 20

CUBE_SIZE = 25
CUBES_NUM = 20
WIDTH = CUBES_NUM * CUBE_SIZE
screen = pygame.display.set_mode((WIDTH, WIDTH))

state = GameState(
    snake=None,
    direction=None,
    food=None,
    field_size=CUBES_NUM
)