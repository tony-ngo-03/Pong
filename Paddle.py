import pygame


class Paddle:
    def __init__(self, pos: pygame.Vector2, speed: float, color, width=15, height=100) -> None:
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos.x, pos.y, width, height)

    def move_up(self):
        self.position.y -= self.speed
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y + self.height > 720:
            self.position.y = 720

    def move_down(self):
        self.position.y += self.speed
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y + self.height > 720:
            self.position.y = 720 - self.height

    def move(self, key: pygame.key):
        if key[pygame.K_w]:  # if the player presses W, then what??
            self.move_up()
        if key[pygame.K_s]:  # if the player presses S, then what??
            self.move_down()
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def draw(self, screen: pygame.surface):
        pygame.draw.rect(screen, "white", self.rect)

    def get_pos(self) -> pygame.Vector2:
        return self.position
