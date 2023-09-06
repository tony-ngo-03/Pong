import random

import pygame

BOTTOM_OOB = 720
TOP_OOB = 0
LEFT_OOB = 0
RIGHT_OOB = 1080


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

    # resets the ball to the center of the screen while getting a random direction
    # pre: ball must have gotten off the screen
    # post: |self.position| changed
    def reset_ball(self) -> None:
        self.position = pygame.Vector2(self.default_pos.x, self.default_pos.y)
        self.speed = self.default_speed
        self.move_left = random.randint(0, 1)
        self.move_down = random.randint(0, 1)



    def did_collide(self, paddle):
        circle_center = (self.position.x + self.radius, self.position.y + self.radius)
        paddle_center = (paddle.position.x + paddle.width // 2, paddle.position.y + paddle.height // 2)
        distance_x = abs(circle_center[0] - paddle_center[0])
        distance_y = abs(circle_center[1] - paddle_center[1])
        if distance_x <= (self.radius + paddle.width // 2) and distance_y <= (self.radius + paddle.height // 2):
            return True
        return False

    # detects if the ball has collided with a paddle, and if so reverse horizontal movement
    # pre: paddle_list is a list of paddles, this_circle != None
    # post: may or may not change direction of ball
    def bounce(self, paddle_list: list) -> bool:
        speed_increase = 1.05
        to_return = False
        for paddle in paddle_list:
            if self.did_collide(paddle):
                self.move_left = not self.move_left
                self.speed *= speed_increase
                to_return = True
        return to_return

    # makes sure the ball does not go off the top and bottom edges of the screen
    # pre: none
    # post: |move_down| may change
    def move_validation(self) -> bool:
        if self.position.y + self.radius > BOTTOM_OOB:
            self.move_down = False
            return True
        if self.position.y - self.radius < TOP_OOB:
            self.move_down = True
            return True
        return False

    # Determines if the ball goes off-screen
    # pre: none
    # post: Return "P" if the player wins, "E" if the enemy wins, and "N" if no one wins
    def get_winner(self) -> str:
        if self.position.x - self.radius > RIGHT_OOB:
            return "P"
        if self.position.x + self.radius < LEFT_OOB:
            return "E"
        return "N"

    # moves the ball by |speed|
    # pre: none
    # post: |position| changed
    def move(self) -> bool:
        if self.move_left:
            self.position.x -= self.speed
        if not self.move_left:
            self.position.x += self.speed
        if self.move_down:
            self.position.y += self.speed
        if not self.move_down:
            self.position.y -= self.speed
        return self.move_validation()

    # draws the ball onto the screen
    # pre: screen is type surface, paddle_list != None
    # post: returns None
    def draw(self, screen: pygame.surface, paddle_list: list) -> bool:
        pygame.draw.circle(screen, self.color, self.position, self.radius)
        return self.bounce(paddle_list)
