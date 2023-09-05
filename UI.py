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




class Score:
    def __init__(self) -> None:
        self.font_size = 32
        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.font_text_color = (255, 255, 255)
        self.font_bg_color = (0, 0, 0)

    def get_rect(self, text: pygame.surface, pos: pygame.Vector2):
        text_rect = text.get_rect()
        text_rect.topleft = pygame.Vector2(pos.x, pos.y)
        return text_rect

    def display_score(self, screen: pygame.surface, player_score: int, enemy_score: int):
        # player score
        player_score_text = self.font.render(str(player_score), True, self.font_text_color, self.font_bg_color)

        player_rect = self.get_rect(player_score_text, pygame.Vector2(0, 0))
        screen.blit(player_score_text, player_rect)

        enemy_score_text = self.font.render(str(enemy_score), True, self.font_text_color, self.font_bg_color)
        enemy_rect = self.get_rect(enemy_score_text, pygame.Vector2(1080 - enemy_score_text.get_width(), 0))
        screen.blit(enemy_score_text, enemy_rect)
