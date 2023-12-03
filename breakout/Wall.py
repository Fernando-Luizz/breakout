import pygame

edge_color = (0, 0, 0)
red_brick = (255, 0, 0)
orange_brick = (255 * 65536 + 165 * 256 + 0)
green_brick = (0, 100, 0)
yelow_brick = (255, 255, 0)

class Wall:
    def __init__(self, screen, screen_width, column, rows):
        self.width = screen_width / column
        self.height = 20
        self.blocks_all_wall = []  #Armazena todos os blocos da parede

        initial_y = 100
        for row in range(rows):
            block_row = []
            for col in range(column):
                brick_x = col * self.width
                brick_y = row * self.height + initial_y
                rect = pygame.Rect(brick_x, brick_y, self.width, self.height) #coordenada(x,y, largura,altura)

                if row < 2:
                    points = 7
                elif 2 <= row < 4:
                    points = 5
                elif 4 <= row < 6:
                    points = 3
                elif row >= 6:
                    points = 1

                # Adiciona o retângulo e a pontuacao à linha de blocos
                block_row.append((rect, points))
            self.blocks_all_wall.append(block_row)

    def draw_wall(self, screen):
        for row in self.blocks_all_wall:
            for brick in row:
                if brick[1] == 7:
                    brick_color = red_brick
                elif brick[1] == 5:
                    brick_color = orange_brick
                elif brick[1] == 3:
                    brick_color = green_brick
                else:
                    brick_color = yelow_brick

                pygame.draw.rect(screen, brick_color, brick[0])
                pygame.draw.rect(screen, edge_color, brick[0], 2) #borda
