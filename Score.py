import pygame


def get_rect(text: pygame.surface, pos: pygame.Vector2):
    text_rect = text.get_rect()
    text_rect.topleft = pygame.Vector2(pos.x, pos.y)
    return text_rect


class Score:
    def __init__(self) -> None:
        self.font_size = 32
        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.font_text_color = (255, 255, 255)
        self.font_bg_color = (0, 0, 0)

    def display_score(self, screen: pygame.surface, player_score: int, enemy_score: int):
        # player score
        player_score_text = self.font.render(str(player_score), True, self.font_text_color, self.font_bg_color)

        player_rect = get_rect(player_score_text, pygame.Vector2(0, 0))
        screen.blit(player_score_text, player_rect)

        enemy_score_text = self.font.render(str(enemy_score), True, self.font_text_color, self.font_bg_color)
        enemy_rect = get_rect(enemy_score_text, pygame.Vector2(1080 - enemy_score_text.get_width(), 0))
        screen.blit(enemy_score_text, enemy_rect)
