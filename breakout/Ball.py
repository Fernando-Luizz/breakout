import pygame
class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.x = ( x - (self.radius))
        self.y = (y - (self.radius))
        self.rect = pygame.Rect(x, y, self.radius * 2, self.radius * 2)
        self.x_speed = 2
        self.y_speed = -2
        self.lost = False

    def draw(self, screen):
        white_ball = (255, 255, 255)
        edge_ball = (0, 0, 0)
        pygame.draw.circle(screen, white_ball, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
        pygame.draw.circle(screen, edge_ball, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius, 2)

    def update_movement(self, screen_width, screen_height, racket):

        if(self.rect.left < 0) or (self.rect.right > screen_width):
            self.x_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1

        if self.rect.bottom > screen_height:
            self.lost = True

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        return self.lost
