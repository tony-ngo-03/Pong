import pygame

import Ball
import Paddle
import UI

# pygame setup
HEIGHT = 720
WIDTH = 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# UI


def initialize_screen():
    global SCREEN

    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG")


def before_game(play_button, title_text):
    global SCREEN
    play_button.display(SCREEN)
    title_text.display(SCREEN)


def reset_game(paddle_list: list, ball_list: list):
    for ball in ball_list:
        ball.reset_ball()
    for paddle in paddle_list:
        paddle.reset_paddle()


def main():
    initialize_screen()
    play_button = UI.Button('PLAY', pygame.Vector2(WIDTH / 2, HEIGHT / 2), 50)
    title_text = UI.Text('PONG', pygame.Vector2(WIDTH / 2, 0), 50)
    introduction = True
    running = True
    desired_frame_rate = 60
    paddle_list = []
    player = Paddle.playerPaddle(pygame.Vector2(15, SCREEN.get_height() // 2), 2.5, "white")
    enemy = Paddle.enemyPaddle(pygame.Vector2(SCREEN.get_width() - (2 * 15), SCREEN.get_height() // 2), 2.5, "white")
    paddle_list.append(player)
    paddle_list.append(enemy)

    ball_list = []
    ball_0 = Ball.Ball(pygame.Vector2(SCREEN.get_width() // 2, SCREEN.get_height() // 2), 2.5, "white")
    ball_list.append(ball_0)

    score = UI.Score()
    player_score = 0
    enemy_score = 0

    title = UI.Text('PONG', pygame.Vector2(SCREEN.get_width() // 2, 0), 32)
    play_button_rect = play_button.get_button()
    while running:
        SCREEN.fill(BLACK)
        if introduction:
            before_game(play_button, title_text)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if introduction and play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    introduction = False

        if not introduction:
            score.display_score(SCREEN, player_score, enemy_score)
            title.display(SCREEN)
            player.move(pygame.key.get_pressed())
            player.draw(SCREEN)
            enemy.move()
            enemy.draw(SCREEN)

            for ball in ball_list:
                ball.move()
                ball.draw(SCREEN, paddle_list)
                winner = ball.off_screen()
                if winner == "P":
                    player_score += 1
                    reset_game(paddle_list, ball_list)
                if winner == "E":
                    enemy_score += 1
                    reset_game(paddle_list, ball_list)

        CLOCK.tick(desired_frame_rate)

        # always flip to draw
        pygame.display.flip()


main()
