import pygame


class Ball:

    def __init__(self, pos: pygame.Vector2, speed: float, color, radius=15):
        self.position = pos
        self.speed = speed
        self.color = color
        self.radius = radius
        self.move_left = True
        self.move_down = True

        self.default_pos = pygame.Vector2(pos.x, pos.y)
        self.default_speed = speed

    def reset_ball(self):
        self.position = pygame.Vector2(self.default_pos.x, self.default_pos.y)
        self.speed = self.default_speed

    def bounce(self, paddle_list: list, this_circle):
        for paddle in paddle_list:
            if this_circle.colliderect(paddle):
                self.move_left = not self.move_left

    def move_validation(self):
        if self.position.y + self.radius > 720:
            self.move_down = False
        if self.position.y - self.radius < 0:
            self.move_down = True

    def off_screen(self) -> bool:
        if self.position.x + self.radius > 1080:
            return True
        if self.position.x - self.radius < 0:
            return True

    def move(self):
        if self.move_left:
            self.position.x -= self.speed
        if not self.move_left:
            self.position.x += self.speed
        if self.move_down:
            self.position.y += self.speed
        if not self.move_down:
            self.position.y -= self.speed
        self.move_validation()

    def draw(self, screen: pygame.surface, paddle_list: list) -> None:
        this_ball = pygame.draw.circle(screen, self.color, self.position, self.radius)
        self.bounce(paddle_list, this_ball)
