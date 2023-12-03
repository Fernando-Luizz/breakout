import pygame
class Ball:
    def __init__(self, x, y):
        self.radius = 10
        self.x = ( x - (self.radius))
        self.y = (y - (self.radius))
        self.rect = pygame.Rect(x, y, self.radius * 2, self.radius * 2)
        self.x_speed = 0.6
        self.y_speed = -0.6
        self.max_speed = 0.8
        self.lost = False
        self.score = 0

    def draw(self, screen):
        white_ball = (255, 255, 255)
        edge_ball = (0, 0, 0)
        pygame.draw.circle(screen, white_ball, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
        pygame.draw.circle(screen, edge_ball, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius, 2)

    def check_racket_collision(self, racket):
        colision_treesh = 5

        if self.rect.colliderect(racket.rect):
            if abs(self.rect.bottom - racket.rect.top) < colision_treesh and self.y_speed > 0:
                self.y_speed *= -1
                self.x_speed += racket.direction

            if self.x_speed > self.max_speed:
                self.x_speed = self.max_speed
            elif self.x_speed < 0 and self.y_speed < -self.max_speed:
                self.x_speed = -self.max_speed

    def wall_collision(self, blocks_all_wall):
        colision_treesh = 5

        for row_cont, row in enumerate(blocks_all_wall):
            for brike_cont, (brike_rect, points) in enumerate(row):
                if self.rect.colliderect(brike_rect):
                    if abs(self.rect.bottom - brike_rect.top) < colision_treesh and self.y_speed > 0:
                        self.y_speed *= -1
                    if abs(self.rect.top - brike_rect.bottom) < colision_treesh and self.y_speed < 0:
                        self.y_speed *= -1

                    if abs(self.rect.right - brike_rect.left) < colision_treesh and self.x_speed > 0:
                        self.x_speed *= -1
                    if abs(self.rect.left - brike_rect.right) < colision_treesh and self.x_speed < 0:
                        self.x_speed *= -1

                    self.update_score(points)
                    blocks_all_wall[row_cont][brike_cont] = ((0, 0, 0, 0), 0) #Tijolo destruido com um toque

    def update_score(self, points):
        if points == 7:
            self.score += 7
        elif points == 5:
            self.score += 5
        elif points == 3:
            self.score += 3
        elif points == 1:
            self.score += 1

    def update_movement(self, screen_width, screen_height, racket, on_racket):
        if on_racket:
            return False  # Retorna False se a bola ainda está na raquete
        self.screen_boundaries(screen_width, screen_height)
        self.check_racket_collision(racket)
        if self.lost:
            return True  # Retorna True se a bola foi perdida

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        return False  # Retorna False se a bola não foi perdida

    def screen_boundaries(self, screen_width, screen_height):
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.x_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1

        if self.rect.bottom > screen_height:
            self.lost = True

    def reset_position(self, x, y):
        self.x = x - self.radius
        self.y = y - self.radius
        self.rect.x = x - self.radius
        self.rect.y = y - self.radius
        self.lost = False
