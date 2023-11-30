import sys
import pygame
from Wall import Wall
from Racket import Racket
from Ball import Ball

black_background = (0, 0, 0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")

brick_wall = Wall(screen, screen_width, 12, 8) #Instancia classe Wall

racket = Racket(screen_width, screen_height, 12) #instancia da classe Racket

ball = Ball(racket.rect.x + ((racket.width // 2)-7.5), racket.rect.y - ((racket.height * 2)-21)) #Determina  aposição inicial da bola#

flag = True
while flag:
    screen.fill(black_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    racket.update_movement(screen_width)     #Atualiza a posição da raquete
    ball.update_movement(screen_width, screen_height, racket) #Atualiza a posição da bola

    brick_wall.draw_wall(screen)  #Desenha a parede de tijolos
    racket.draw(screen)#Desenha a raquete
    ball.draw(screen) #Desenha a bola

    pygame.display.update()

pygame.quit()
sys.exit()
