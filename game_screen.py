import pygame
from pygame.examples.moveit import HEIGHT

from game_variables import screen, WIDTH, BLACK, RED, state, BROWN_DART, GREEN_2_DART, WHITE


def select_name():
    font = pygame.font.SysFont("Press Start 2P", 20)
    font_author = pygame.font.SysFont("Press Start 2P", 10)

    input_box = pygame.Rect(WIDTH / 2 - 110, WIDTH / 2 + 25, 200, 30)

    color_inactive = pygame.Color(BROWN_DART)
    color_active = pygame.Color(GREEN_2_DART)
    color = color_inactive

    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    else:
                        text += event.unicode

        background = pygame.image.load('static/snake_screen.png')
        background = pygame.transform.scale(background, (WIDTH, WIDTH))
        screen.blit(background, (0, 0))

        txt_player_name = font.render("Your Name:", True, GREEN_2_DART)
        txt_author_game = font_author.render("Created by: Sebastian Ledzianowski", True, WHITE)

        txt_surface = font.render(text, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        screen.blit(txt_player_name, (input_box.x + 5, input_box.y - 25))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        screen.blit(txt_author_game, (input_box.x - 170, input_box.y + 250))

        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()


def select_speed_game():
    background = pygame.image.load('static/dart_screen.png')
    background = pygame.transform.scale(background, (WIDTH, WIDTH))
    screen.blit(background, (0, 0))

    font_title = pygame.font.SysFont("Press Start 2P", 30)
    font_options = pygame.font.SysFont("Press Start 2P", 20)

    title = font_title.render("Game Level:", True, BROWN_DART)
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4))

    easy = font_options.render("Easy - Press 1", True, BLACK)
    medium = font_options.render("Medium - Press 2", True, BLACK)
    hard = font_options.render("Hard - Press 3", True, BLACK)

    screen.blit(easy, (WIDTH / 2 - easy.get_width() / 2, HEIGHT / 2))
    screen.blit(medium, (WIDTH / 2 - medium.get_width() / 2, HEIGHT / 2 + 50))
    screen.blit(hard, (WIDTH / 2 - hard.get_width() / 2, HEIGHT / 2 + 100))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state.speed = 5
                    waiting = False
                elif event.key == pygame.K_2:
                    state.speed = 10
                    waiting = False
                elif event.key == pygame.K_3:
                    state.speed = 15
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    state.start_game = False
    return state.speed


def game_over_screen(score, player_name):
    background = pygame.image.load('static/game_over_screen.png')
    background = pygame.transform.scale(background, (WIDTH, WIDTH))
    screen.blit(background, (0, 0))

    font_game_over = pygame.font.SysFont("Press Start 2P", 35)
    text_game_over = font_game_over.render("Game Over", True, RED)
    text_rect_game_over = text_game_over.get_rect(center=(WIDTH / 2, WIDTH / 4))

    font_score = pygame.font.SysFont("Press Start 2P", 20)
    text_score = font_score.render(f"{player_name} this your score: {score}", True, BLACK)
    test_rect_score = text_score.get_rect(center=(WIDTH / 2, WIDTH / 3 + 40))

    font_control = pygame.font.SysFont("Press Start 2P", 15)
    text_control_enter = font_control.render("(ENTER) to Return", True, BROWN_DART)
    text_control_space = font_control.render("(SPACE) to Restart", True, BROWN_DART)
    text_control_escape = font_control.render("(ESCAPE) to Quit", True, BROWN_DART)
    text_rect_control_enter = text_control_enter.get_rect(center=(WIDTH / 2, (WIDTH / 3) * 2 - 40))
    text_rect_control_space = text_control_space.get_rect(center=(WIDTH / 2, (WIDTH / 3) * 2 - 20))
    text_rect_control_escape = text_control_escape.get_rect(center=(WIDTH / 2, (WIDTH / 3) * 2))

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state.set_initial_position()
                    state.start_game = False
                    state.game_over = False
                    waiting = False
                if event.key == pygame.K_SPACE:
                    state.start_game = True
                    state.game_over = False
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        screen.blit(text_game_over, text_rect_game_over)
        screen.blit(text_score, test_rect_score)
        screen.blit(text_control_enter, text_rect_control_enter)
        screen.blit(text_control_space, text_rect_control_space)
        screen.blit(text_control_escape, text_rect_control_escape)


        pygame.display.flip()