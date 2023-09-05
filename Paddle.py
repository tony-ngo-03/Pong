import pygame


class playerPaddle:
    def __init__(self, pos: pygame.Vector2, speed: float, color, width=15, height=100) -> None:
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.default_position = pygame.Vector2(pos.x, pos.y)
        self.default_speed = speed

    def reset_paddle(self) -> None:
        self.position = pygame.Vector2(self.default_position.x, self.default_position.y)
        self.speed = self.default_speed

    def correct_position(self):
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y + self.height > 720:
            self.position.y = 720 - self.height

    def move_up(self):
        self.position.y -= self.speed

    def move_down(self):
        self.position.y += self.speed

    def move(self, key: pygame.key):
        upwards_key = pygame.K_w
        downwards_key = pygame.K_s
        if key[upwards_key]:
            self.move_up()
        if key[downwards_key]:
            self.move_down()
        self.correct_position()

    def draw(self, screen: pygame.surface):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)


class enemyPaddle:
    def __init__(self, pos: pygame.Vector2, speed: float, color, width=15, height=100) -> None:
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.default_position = pygame.Vector2(pos.x, pos.y)
        self.default_speed = speed

        # control
        self.enemy_control = True

    def reset_paddle(self) -> None:
        self.position = pygame.Vector2(self.default_position.x, self.default_position.y)
        self.speed = self.default_speed

    def correct_position(self) -> bool:
        if self.position.y < 0:
            self.position.y = 0
            return True
        if self.position.y + self.height > 720:
            self.position.y = 720 - self.height
            return True
        return False

    def move_up(self):
        self.position.y -= self.speed

    def move_down(self):
        self.position.y += self.speed

    def move(self):
        if self.enemy_control:
            self.move_down()
        else:
            self.move_up()
        if self.correct_position():
            self.enemy_control = not self.enemy_control

    def draw(self, screen: pygame.surface):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
