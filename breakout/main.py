import sys
import pygame
from Brick import Brick
from Racket import Racket
from Ball import Ball
from Edge import Edge
import pygame.font

columns = 14
rows = 8
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
black_background = (0, 0, 0)
red_message = (255, 0, 0)
green_message = (0, 255, 0)
white_score = (255, 255, 255)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")
lives = 3
score = 0

brick_wall = Brick(screen, screen_width-19, columns, rows) #Instância classe Brick
racket = Racket(screen_width, screen_height, columns) #Instância da classe Racket
initial_ball_position = ( #Posição inicial da bola
    racket.rect.x + ((racket.width // 2) - 7.5),
    racket.rect.y - ((racket.height * 2) - 21),
     )
ball = Ball(*initial_ball_position)
edge = Edge()

# Load fonts outside the loop
font_size = 36
game_font = pygame.font.Font("assets/font/game_font.ttf", font_size)
score_font = pygame.font.Font("assets/font/score_font.ttf", 36)

new_wall_needed = False
ball_on_racket = True


flag = True
while flag and lives > 0:
    screen.fill(black_background)

    edge.edge()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    racket.update_movement(screen_width)

    if ball_on_racket:
        ball.rect.x = racket.rect.x + (racket.width // 2) - 7.5
        ball.rect.y = racket.rect.y - ((racket.height * 2) - 21)

    #Atualização do movimento da bola e verificação de colisões
    lost_life = ball.update_movement(screen_width, screen_height, racket, ball_on_racket)
    if lost_life:
        lives -= 1
        if lives > 0:
            ball_on_racket = True
            ball.reset_position(
                racket.rect.x + (racket.width // 2) - 7.5,
                racket.rect.y - ((racket.height * 2) - 21),
            )
    else:
        ball_on_racket = False

    ball.check_racket_collision(racket)
    ball.wall_collision(brick_wall.blocks_all_wall)

    brick_wall.draw_wall(screen) #Desenha a parede de tijolos
    racket.draw(screen) #Desenha a raquete
    ball.draw(screen) #Desenha a bola

    lives_text = score_font.render(f" {lives}", True, white_score)
    screen.blit(lives_text, (80, 40))
    score_text = score_font.render(f" {ball.score}", True, white_score)
    screen.blit(score_text, (650, 40))
    if all(all(brick[1] == 0 for brick in row) for row in brick_wall.blocks_all_wall): #Verifica se todos os tijolos foram destruídos
        if new_wall_needed:
            flag = False
        else:
            new_wall_needed = True
            brick_wall = Wall(screen, screen_width, columns, rows)

    pygame.display.update()

if lives == 0:
    message = "GAME OVER"
    
elif not flag:
    message = "YOU WON!"

screen.fill(black_background)
font = pygame.font.Font("assets/font/game_font.ttf", 72)
text = font.render(message, True, red_message if lives == 0 else green_message)
screen.blit(text, (screen_width // 2 - 150, screen_height // 2 - 36))

#Mostra a pontuacao final
score_text = game_font.render(f"Score: {ball.score}", True, white_score)
screen.blit(score_text, (screen_width // 2 - 150, screen_height // 2 + 36))

pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
sys.exit()
