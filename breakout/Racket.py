import pygame
from pygame.locals import Rect
class Racket:
    def __init__(self, screen_width, screen_height, column):
        self.height = 20
        self.width = int(screen_width / column)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 5
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

    def update_movement(self, screen_width):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        color_racket = (135, 206, 250)
        pygame.draw.rect(screen, color_racket, self.rect)
