import pygame


class playerPaddle:
    def __init__(self, pos: pygame.Vector2, speed: float, color, width=15, height=100) -> None:
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.default_speed = speed

    def reset_paddle(self) -> None:
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
        self.default_speed = speed

        # control
        self.enemy_control = True

    def reset_paddle(self) -> None:
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

    def easy_move(self):
        if self.enemy_control:
            self.move_down()
        else:
            self.move_up()
        if self.correct_position():
            self.enemy_control = not self.enemy_control

    def medium_move(self, ball, height):
        time_to_reach_enemy = (self.position.x - ball.position.x) / ball.speed
        predicted_y = ball.position.y + (ball.speed / 2) * time_to_reach_enemy
        while predicted_y < 0 or predicted_y > height:
            if predicted_y < 0:
                predicted_y = -predicted_y
            else:
                predicted_y = height - predicted_y
        if predicted_y > self.position.y + self.height / 2:
            self.position.y += self.speed
        elif predicted_y < self.position.y + self.height / 2:
            self.position.y -= self.speed
        self.correct_position()

    def hard_move(self, ball):
        self.position.y = ball.position.y
        self.correct_position()

    def move(self, difficulty, ball):
        if difficulty == 'e':
            self.easy_move()
        elif difficulty == 'm':
            self.medium_move(ball, 720)
        else:
            self.hard_move(ball)

    def draw(self, screen: pygame.surface):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
