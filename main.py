import pygame

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


def display_text(message: str, font_size: int, x: int, y: int, font='freesansbold.ttf',  anti_alias=True):
    text_font = pygame.font.Font(font, font_size)
    text = text_font.render(message, anti_alias, WHITE, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    SCREEN.blit(text, text_rect)


def display_button():
    pass


def before_game():
    display_text('PONG', 50, (WIDTH // 2), (HEIGHT // 4))


def main():
    initialize_screen()

    introduction = True
    running = True
    desired_frame_rate = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse clicked")

        SCREEN.fill(BLACK)
        if introduction:
            before_game()
        CLOCK.tick(desired_frame_rate)

        # always flip to draw
        pygame.display.flip()


main()
