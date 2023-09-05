import pygame


class Text:
    def __init__(self, message: str, pos: pygame.Vector2, font_size: int, font_color=(255, 255, 255),
                 font_bg_color=(0, 0, 0), font="freesansbold.ttf") -> None:
        self.message = message
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.font_bg_color = font_bg_color
        self.font = pygame.font.Font(font, self.font_size)

    def display(self, screen: pygame.surface):
        text_to_display = self.font.render(self.message, True, self.font_color, self.font_bg_color)
        text_rect = text_to_display.get_rect()
        text_rect.midtop = self.pos
        screen.blit(text_to_display, text_rect)
