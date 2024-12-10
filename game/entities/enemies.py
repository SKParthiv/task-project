import pygame
import math
from ..constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        super().__init__()
        self.enemy_type = enemy_type
        self.hp = ENEMIES[enemy_type]['hp']
        self.speed = ENEMIES[enemy_type]['speed']
        self.damage = ENEMIES[enemy_type]['damage']
        
        # Create circular enemy
        size = GRID_SIZE
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (size//2, size//2), size//2)
        self.rect = self.image.get_rect(center=(x, y))
        
        # Target the core
        self.target_x = WINDOW_WIDTH // 2
        self.target_y = WINDOW_HEIGHT // 2
        
    def update(self):
        # Move towards core
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist * self.speed
            dy = dy / dist * self.speed
            self.rect.x += dx
            self.rect.y += dy
            
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.kill()