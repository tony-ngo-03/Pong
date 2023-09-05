import pygame


class Text:
    def __init__(self, message: str, pos: pygame.Vector2, font_size: int, font_color=(255, 255, 255),
                 font_bg_color=(0, 0, 0)) -> None:
        self.message = message
        self.pos = pos
        self.font_size = font_size
        self.font_color = font_color
        self.font_bg_color = font_bg_color
        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.text = self.font.render(self.message, True, self.font_color, self.font_bg_color)

    def get_rect(self, position: str):
        text_rect = self.text.get_rect()
        if position == 'midtop':
            text_rect.midtop = self.pos
        if position == 'topleft':
            text_rect.midleft = self.pos
        return text_rect

    def display(self, screen: pygame.surface):
        screen.blit(self.text, self.get_rect('midtop'))


class Button:
    def __init__(self, message: str, pos: pygame.Vector2, font_size, font_color=(0, 0, 0),
                 bg_color=(255, 255, 255)) -> None:
        self.text = Text(message, pos, font_size, font_color, bg_color)

    def display(self, screen: pygame.surface):
        self.text.display(screen)

    def get_button(self):
        return self.text.get_rect('midtop')


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
