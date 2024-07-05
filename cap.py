import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes
screen = pygame.display.set_mode((1280, 720))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
TILE_SIZE = 20

# Labirinto
maze = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "         #      #            ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#...##................##...#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Posições iniciais
pacman_pos = [1 * TILE_SIZE, 1 * TILE_SIZE]
pacman_speed = TILE_SIZE
direction = (0, 0)

# Função para desenhar o labirinto
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '#':
                pygame.draw.rect(screen, BLUE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == '.':
                pygame.draw.circle(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 3)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    draw_maze()    
    pygame.draw.circle(screen, YELLOW, (pacman_pos[0] + TILE_SIZE // 2, pacman_pos[1] + TILE_SIZE // 2), TILE_SIZE // 2)
    # Atualizar o display
    pygame.display.flip()

    # Controlar a taxa de quadros
    pygame.time.Clock().tick(10)