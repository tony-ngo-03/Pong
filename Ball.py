import pygame


class Ball:
    # constructor of Ball
    # pre: pos is type Vector2, speed is type float
    def __init__(self, pos: pygame.Vector2, speed: float, color, radius=15) -> None:
        # basic information for ball
        self.position = pos
        self.speed = speed
        self.color = color
        self.radius = radius
        # control movement
        self.move_left = True
        self.move_down = True
        # resetting information
        self.default_pos = pygame.Vector2(pos.x, pos.y)
        self.default_speed = speed

    # resets the ball to the center of the screen while retaining current direction
    # pre: ball must have gotten off the screen
    # post: |self.position| changed
    def reset_ball(self) -> None:
        self.position = pygame.Vector2(self.default_pos.x, self.default_pos.y)
        self.speed = self.default_speed

    # detects if the ball has collided with a paddle, and if so reverse horizontal movement
    # pre: paddle_list is a list of paddles, this_circle != None
    # post: may or may not change direction of ball
    def bounce(self, paddle_list: list, this_circle) -> None:
        for paddle in paddle_list:
            if this_circle.colliderect(paddle):
                self.move_left = not self.move_left

    # makes sure the ball does not go off the top and bottom edges of the screen
    # pre: none
    # post: |move_down| may change
    def move_validation(self) -> None:
        if self.position.y + self.radius > 720:
            self.move_down = False
        if self.position.y - self.radius < 0:
            self.move_down = True

    # gives us an indication if the ball goes off the screen horizontally
    # pre: none
    # post: return True if we go off the screen horizontally, False otherwise
    def off_screen(self) -> str:
        if self.position.x + self.radius > 1080:
            return "P"
        if self.position.x - self.radius < 0:
            return "E"
        return "N"

    # moves the ball by |speed|
    # pre: none
    # post: |position| changed
    def move(self) -> None:
        if self.move_left:
            self.position.x -= self.speed
        if not self.move_left:
            self.position.x += self.speed
        if self.move_down:
            self.position.y += self.speed
        if not self.move_down:
            self.position.y -= self.speed
        self.move_validation()

    # draws the ball onto the screen
    # pre: screen is type surface, paddle_list != None
    # post: returns None
    def draw(self, screen: pygame.surface, paddle_list: list) -> None:
        this_ball = pygame.draw.circle(screen, self.color, self.position, self.radius)
        self.bounce(paddle_list, this_ball)
