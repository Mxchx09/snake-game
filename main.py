import pygame

pygame.init()

WIN_HEIGHT, WIN_WIDTH = 500, 500
GRID_SIZE = 20  # Anzahl der Blöcke pro Reihe/Spalte
BLOCK_SIZE = WIN_WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

class Grid:
    def __init__(self, grid_x):
        self.grid_x = grid_x
        self.grid = [[0] * grid_x for _ in range(grid_x)]  # 2D-Liste für die Farben

    def draw_grid(self, win):
        for i in range(self.grid_x):
            pygame.draw.line(win, (255, 255, 255), (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, WIN_HEIGHT), 3)
            pygame.draw.line(win, (255, 255, 255), (0, i * BLOCK_SIZE), (WIN_WIDTH, i * BLOCK_SIZE), 3)

    def draw_blocks(self, win):
        for y in range(self.grid_x):
            for x in range(self.grid_x):
                if self.grid[y][x] == 1:  # Falls das Feld aktiviert ist
                    pygame.draw.rect(win, (0, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def add_block(self, pos):
        x = pos[0] // BLOCK_SIZE  # Spalte bestimmen
        for y in range(self.grid_x - 1, -1, -1):  # Von unten nach oben prüfen
            if self.grid[y][x] == 0:  # Leeres Feld gefunden
                self.grid[y][x] = 1  # Block setzen
                return  # Beende die Funktion nach dem ersten Treffer


def main(FPS=60):
    running = True
    clock = pygame.time.Clock()
    
    grid = Grid(GRID_SIZE)
    
    while running:
        screen.fill((0, 0, 0))  # Hintergrund schwarz
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid.add_block(pygame.mouse.get_pos())

        grid.draw_blocks(screen)
        grid.draw_grid(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    exit()

main()
