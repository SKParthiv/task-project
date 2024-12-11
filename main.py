import pygame
from game.core import Game
from game.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Strategy Defense Game")
    clock = pygame.time.Clock()
    
    game = Game(screen)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
            
        game.update()
        game.draw()
        
        pygame.display.flip()
        clock.tick(FPS)
        
        if game.core_hp <= 0:
            running = False
            print("Game Over")
        
    pygame.quit()

if __name__ == "__main__":
    main()