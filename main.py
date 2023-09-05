import pygame

import Ball
import Paddle
import Score
import UI

# pygame setup
HEIGHT = 720
WIDTH = 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def initialize_screen():
    global SCREEN

    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG")


def display_text(message: str, font_size: int, x: int, y: int, text_color=WHITE, background=BLACK,
                 font='freesansbold.ttf',
                 anti_alias=True):
    text_font = pygame.font.Font(font, font_size)
    text = text_font.render(message, anti_alias, text_color, background)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    SCREEN.blit(text, text_rect)
    return text_rect


def display_button():
    button = display_text("PLAY", 40, (WIDTH // 2), (HEIGHT // 4) + 200, BLACK, WHITE)
    return button


def before_game():
    display_text('PONG', 50, (WIDTH // 2), (HEIGHT // 4))


def reset_game(paddle_list: list, ball_list: list):
    for ball in ball_list:
        ball.reset_ball()
    for paddle in paddle_list:
        paddle.reset_paddle()


def main():
    initialize_screen()
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

    score = Score.Score()
    player_score = 0
    enemy_score = 0

    title = UI.Text('PONG', pygame.Vector2(SCREEN.get_width() // 2, 0), 32)
    while running:
        SCREEN.fill(BLACK)
        if introduction:
            before_game()
            play_button = display_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if introduction is true then play_button can never be None
                if introduction and play_button.collidepoint(pygame.mouse.get_pos()):
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
