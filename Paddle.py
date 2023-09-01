import pygame


class Paddle:
    def __init__(self, pos: pygame.Vector2, speed: float, color, is_human, width=15, height=100) -> None:
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos.x, pos.y, width, height)
        self.is_player = is_human
        self.control_enemy = False

        self.default_pos = pygame.Vector2(pos.x, pos.y)
        self.default_speed = speed

    def reset_paddle(self):
        self.position = pygame.Vector2(self.default_pos.x, self.default_pos.y)
        self.speed = self.default_speed

    def position_check(self) -> bool:
        top_of_screen = 0
        bottom_of_screen = 720
        if self.position.y < top_of_screen:
            self.position.y = top_of_screen
            return True
        if self.position.y + self.height > bottom_of_screen:
            self.position.y = bottom_of_screen - self.height
            return True
        return False

    def move_up(self) -> bool:
        self.position.y -= self.speed
        return self.position_check()

    def move_down(self) -> bool:
        self.position.y += self.speed
        return self.position_check()

    def move(self, key: pygame.key):
        if self.is_player:
            if key[pygame.K_w]:
                self.move_up()
            if key[pygame.K_s]:
                self.move_down()
        else:
            if self.control_enemy:
                if self.move_down():
                    self.control_enemy = not self.control_enemy
            else:
                if self.move_up():
                    self.control_enemy = not self.control_enemy
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def draw(self, screen: pygame.surface):
        pygame.draw.rect(screen, "white", self.rect)

    def get_pos(self) -> pygame.Vector2:
        return self.position
