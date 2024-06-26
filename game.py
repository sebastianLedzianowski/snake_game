import pygame

from direction import Direction
from game_draw import draw, fill_bg
from game_screen import game_over_screen, select_name, select_speed_game
from game_variables import state, screen

state.set_initial_position()

clock = pygame.time.Clock()
background = fill_bg()

while True:
    clock.tick(state.speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state.turn(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                state.turn(Direction.RIGHT)
            elif event.key == pygame.K_UP:
                state.turn(Direction.UP)
            elif event.key == pygame.K_DOWN:
                state.turn(Direction.DOWN)


    if state.start_game is True:
        player_name = select_name()
        select_speed_game()
    elif state.game_over is True:
        game_over_screen(state.score, player_name)
    else:
        state.step()
        screen.blit(background, (0, 0))
        draw(state.snake, state.food, state.score)
