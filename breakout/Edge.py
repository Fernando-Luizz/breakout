import pygame

edge_color = (212, 210, 212)
red_brick = (162, 8, 0)
orange_brick = (183, 119, 0)
green_brick = (0, 127, 33)
yellow_brick = (197, 199, 37)
racket_color = (0, 97, 148)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

wall_width = 10
racket_height = 20
brick_height = 20
x_gap = 7
y_gap = 5

class Edge():
	def edge(a):
		pygame.draw.line(screen, edge_color, [0, 0], [screen_width, 0], 45) #Desenha a borda cinza do topo
		pygame.draw.line(screen, edge_color, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, screen_height], wall_width) #Desenha a borda lateral esquerda
		pygame.draw.line(screen, edge_color, [(screen_width - wall_width / 2) - 1, 0], [(screen_width - wall_width / 2) - 1, screen_height], wall_width) #Desenha a borda lateral direita

		pygame.draw.line(screen, racket_color, [(wall_width / 2) - 1, 35 + screen_height - 65 + racket_height / 2 - 54 / 2], [(wall_width / 2) - 1, 15 + screen_height - 65 + racket_height / 2 - 54 / 2 + 54], wall_width)
		pygame.draw.line(screen, racket_color, [(screen_width - wall_width / 2) - 1, 35 + screen_height - 65 + racket_height / 2 - 54 / 2], [(screen_width - wall_width / 2) - 1, 15 + screen_height - 65 + racket_height / 2 - 54 / 2 + 54], wall_width)

		pygame.draw.line(screen, red_brick, [(wall_width / 2) - 1, 100], [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap-121], wall_width)
		pygame.draw.line(screen, red_brick, [(screen_width - wall_width / 2) - 1, 100], [(screen_width - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap-121], wall_width)

		pygame.draw.line(screen, orange_brick, [(wall_width / 2) - 1, 90 + 2 * brick_height + 2 * y_gap], [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap-134], wall_width)
		pygame.draw.line(screen, orange_brick, [(screen_width - wall_width / 2) - 1, 90 + 2 * brick_height + 2 * y_gap], [(screen_width - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap-134], wall_width)

		pygame.draw.line(screen, green_brick, [(wall_width / 2) - 1, 78 + 4 * brick_height + 4 * y_gap], [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap-144], wall_width)
		pygame.draw.line(screen, green_brick, [(screen_width - wall_width / 2) - 1, 78 + 4 * brick_height + 4 * y_gap], [(screen_width - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap-144], wall_width)

		pygame.draw.line(screen, yellow_brick, [(wall_width / 2) - 1, 69 + 6 * brick_height + 6 * y_gap], [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap-154], wall_width)
		pygame.draw.line(screen, yellow_brick, [(screen_width - wall_width / 2) - 1, 69 + 6 * brick_height + 6 * y_gap], [(screen_width - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap-154], wall_width)