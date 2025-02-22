
WIN_HEIGHT, WIN_WIDTH = 500, 500
class Grid:
    def __init__(self, grid_x):
        self.block_size = WIN_WIDTH // grid_x
        self.grid_x = grid_x
        self.grid = [[0] * self.block_size for _ in range(1, self.grid_x)]
    

    def draw_grid(self, win):
        for i in range(1, self.grid_x):
            pygame.draw.line(win, (255, 255, 255), (i * self.block_size, 0), (i * self.block_size, WIN_HEIGHT), 3)
            pygame.draw.line(win, (255, 255, 255), (0, i * self.block_size), (WIN_WIDTH, i * self.block_size), 3)
            
    def color_block(self):
        for pos, i in enumerate(self.grid):
            print(pos, i)
            
grid = Grid(10)

grid.color_block()