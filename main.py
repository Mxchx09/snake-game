import pygame

pygame.init()

WIN_HEIGHT, WIN_WIDTH = 500, 500

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

def create_grid():
    grid = [[0] * 10 for _ in range(1, 11)]
    return grid

def draw_grid(win):
    for i in range(1, 10):
        pygame.draw.line(win, (255, 255, 255), (i * 50, 0), (i * 50, WIN_HEIGHT), 3)
        pygame.draw.line(win, (255, 255, 255), (0, i * 50), (WIN_WIDTH, i * 50), 3)
        
def fill_grid(grid):
    for i in range(len(grid)):
        pass
        

    

def main(FPS=120):
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
        draw_grid(screen)
                
        pygame.display.flip()
    pygame.exit()
    exit()
    
main()