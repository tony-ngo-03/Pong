import pygame


class Paddle:
    def __init__(self, pos: pygame.Vector2, speed: float, color, width=15, height=100) -> None:
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height

    def move(self):
        pass
    def get_pos(self) -> pygame.Vector2:
        return self.position

