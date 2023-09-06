import pygame

import Ball
import Paddle
import UI
import Music

# pygame setup
pygame.init()
WIDTH = 1080
HEIGHT = 720
DESIRED_FRAME_FRATE = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - tony-ngo-03")
CLOCK = pygame.time.Clock()

# Sound FX setup
Music.init()

# COLORS for constants.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def reset_game(paddle_list: list, ball_list: list):
    delay_after_win_ms = 500
    Music.score()
    pygame.time.delay(delay_after_win_ms)
    for ball in ball_list:
        ball.reset_ball()
    for paddle in paddle_list:
        paddle.reset_paddle()


def get_paddle_list():
    paddle_list = [Paddle.playerPaddle(pygame.Vector2(15, SCREEN.get_height() // 2), 2.5, "white"),
                   Paddle.enemyPaddle(pygame.Vector2(SCREEN.get_width() - (2 * 15), SCREEN.get_height() // 2), 2.5,
                                      "white")]
    return paddle_list


def get_ball_list():
    ball_list = [Ball.Ball(pygame.Vector2(SCREEN.get_width() // 2, SCREEN.get_height() // 2), 2.5, "white")]
    return ball_list


def show_introduction():
    font_size = 50
    play_button = UI.Button('PLAY', pygame.Vector2(WIDTH / 2, HEIGHT / 2), font_size)
    title_text = UI.Text('PONG', pygame.Vector2(WIDTH / 2, 0), font_size)
    introduction_control = True
    while introduction_control:
        SCREEN.fill(BLACK)
        play_button.display(SCREEN)
        title_text.display(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.get_button().collidepoint(pygame.mouse.get_pos()):
                    introduction_control = False
        CLOCK.tick(DESIRED_FRAME_FRATE)
        pygame.display.flip()


def show_difficulty_selection():
    pass


def show_game_ui(score_ui, title_ui, player_score, enemy_score):
    score_ui.display_score(SCREEN, player_score, enemy_score)
    title_ui.display(SCREEN)


def handle_paddles(paddle_list):
    for paddle in paddle_list:
        paddle.move(pygame.key.get_pressed())
        paddle.draw(SCREEN)


def handle_ball_movement(ball_list, paddle_list):
    for ball in ball_list:
        if ball.move():
            Music.wall_hit()
        if ball.draw(SCREEN, paddle_list):
            Music.paddle_hit()


def handle_paddle_win(ball_list, paddle_list, player_score, enemy_score):
    for ball in ball_list:
        winner = ball.get_winner()
        if winner == "P":
            player_score += 1
            reset_game(paddle_list, ball_list)
        if winner == "E":
            enemy_score += 1
            reset_game(paddle_list, ball_list)
    return player_score, enemy_score


def initialize_game_ui():
    return UI.Score(), UI.Text('PONG', pygame.Vector2(SCREEN.get_width() // 2, 0), 32)


def initialize_scores():
    return 0, 0


def play():
    running = Tr
    ue
    paddle_list = get_paddle_list()
    ball_list = get_ball_list()
    score_ui, title_ui = initialize_game_ui()
    player_score, enemy_score = initialize_scores()
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        show_game_ui(score_ui, title_ui, player_score, enemy_score)
        handle_paddles(paddle_list)

        handle_ball_movement(ball_list, paddle_list)
        player_score, enemy_score = handle_paddle_win(ball_list, paddle_list, player_score, enemy_score)

        CLOCK.tick(DESIRED_FRAME_FRATE)
        # always flip to draw
        pygame.display.flip()
