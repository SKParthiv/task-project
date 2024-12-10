import pygame
from ..constants import *

class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y, mine_type):
        super().__init__()
        self.mine_type = mine_type
        self.interval = MINES[mine_type]['interval']
        self.timer = 0
        self.rect = pygame.Rect(x, y, GRID_SIZE * 3, GRID_SIZE * 3)
        
    def update(self):
        self.timer += 1/FPS
        if self.timer >= self.interval:
            self.timer = 0
            self.generate_gold()
            
    def generate_gold(self):
        return 1  # Generate 1 gold per interval