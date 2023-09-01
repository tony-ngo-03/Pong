import pygame


class Paddle:
    # constructor for the Paddle class
    # pre: pos is type Vector2, speed is type float, is_human True for the player
    def __init__(self, pos: pygame.Vector2, speed: float, color, is_human, width=15, height=100) -> None:
        # basic information about the paddle
        self.position = pos
        self.speed = speed
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos.x, pos.y, width, height)
        # with player/enemy movement
        self.is_player = is_human
        self.control_enemy = False

        # reset information
        self.default_pos = pygame.Vector2(pos.x, pos.y)
        self.default_speed = speed

    # reverts the current position to the starting
    # pre: the ball has gone past the paddle
    # post: returns None, paddle is now at middle of the screen
    def reset_paddle(self):
        self.position = pygame.Vector2(self.default_pos.x, self.default_pos.y)
        self.speed = self.default_speed

    # makes sure that the paddle is not out of bounds
    # pre: none
    # post: returns True if paddle are out of bounds, False otherwise
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

    # moves the paddle |self.speed| vertically upwards
    # pre: none
    # post: returns True if paddle is out of bounds, False otherwise
    def move_up(self) -> bool:
        self.position.y -= self.speed
        return self.position_check()

    # moves the paddle |self.speed| vertically downwards
    # pre: none
    # post: returns True if paddle is out of bounds, False otherwise
    def move_down(self) -> bool:
        self.position.y += self.speed
        return self.position_check()

    # moves the paddle vertically upwards or downwards depending on input
    # pre: key is type pygame.key
    # post: moves the paddle
    def move(self, key: pygame.key):
        upwards_key = pygame.K_w
        downwards_key = pygame.K_s
        if self.is_player:
            if key[upwards_key]:
                self.move_up()
            if key[downwards_key]:
                self.move_down()
        else:
            if self.control_enemy:
                if self.move_down():
                    self.control_enemy = not self.control_enemy
            else:
                if self.move_up():
                    self.control_enemy = not self.control_enemy
        # always remake the rect to see changes.
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    # draws the paddle onto the screen
    # pre: screen != None, screen is type surface
    # post: paddle is drawn onto the screen
    def draw(self, screen: pygame.surface):
        pygame.draw.rect(screen, "white", self.rect)

    # getter method for the position if needed
    # TODO: get rid if needed
    def get_pos(self) -> pygame.Vector2:
        return self.position
