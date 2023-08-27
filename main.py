import pygame
import Paddle
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


def display_text(message: str, font_size: int, x: int, y: int, text_color=WHITE, background=BLACK, font='freesansbold.ttf',
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


def main():
    initialize_screen()
    introduction = True
    running = True
    desired_frame_rate = 60
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

        CLOCK.tick(desired_frame_rate)

        # always flip to draw
        pygame.display.flip()


main()
