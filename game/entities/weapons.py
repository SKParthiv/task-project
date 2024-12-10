import pygame
import math
from ..constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()
        self.hp = hp
        self.rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.kill()

class Torrent(Weapon):
    def __init__(self, x, y):
        super().__init__(x, y, WEAPONS['torrent']['hp'])
        self.angle = 0
        self.fire_timer = 0
        
    def update(self):
        self.angle += 2
        self.fire_timer += 1/FPS
        if self.fire_timer >= WEAPONS['torrent']['fire_rate']:
            self.fire_timer = 0
            self.shoot()
            
    def shoot(self):
        # Implement shooting logic
        pass

# Implement other weapon classes (DoubleTorrent, QuadTorrent, etc.)