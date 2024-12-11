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
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        self.groups()[0].add(bullet)

class DoubleTorrent(Weapon):
    def __init__(self, x, y):
        super().__init__(x, y, WEAPONS['double_torrent']['hp'])
        self.angle = 0
        self.fire_timer = 0
        
    def update(self):
        self.angle += 2
        self.fire_timer += 1/FPS
        if self.fire_timer >= WEAPONS['double_torrent']['fire_rate']:
            self.fire_timer = 0
            self.shoot()
            
    def shoot(self):
        bullet1 = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        bullet2 = Bullet(self.rect.centerx, self.rect.centery, self.angle + 180)
        self.groups()[0].add(bullet1, bullet2)

class QuadTorrent(Weapon):
    def __init__(self, x, y):
        super().__init__(x, y, WEAPONS['quad_torrent']['hp'])
        self.angle = 0
        self.fire_timer = 0
        
    def update(self):
        self.angle += 2
        self.fire_timer += 1/FPS
        if self.fire_timer >= WEAPONS['quad_torrent']['fire_rate']:
            self.fire_timer = 0
            self.shoot()
            
    def shoot(self):
        bullet1 = Bullet(self.rect.centerx, self.rect.centery, self.angle)
        bullet2 = Bullet(self.rect.centerx, self.rect.centery, self.angle + 90)
        bullet3 = Bullet(self.rect.centerx, self.rect.centery, self.angle + 180)
        bullet4 = Bullet(self.rect.centerx, self.rect.centery, self.angle + 270)
        self.groups()[0].add(bullet1, bullet2, bullet3, bullet4)

class Trap(Weapon):
    def __init__(self, x, y):
        super().__init__(x, y, WEAPONS['trap']['hp'])
        
    def update(self):
        pass  # Traps do not need to update

    def explode(self, enemies):
        for enemy in enemies:
            dx = enemy.rect.centerx - self.rect.centerx
            dy = enemy.rect.centery - self.rect.centery
            distance = math.hypot(dx, dy)
            if distance <= WEAPONS['trap']['radius']:
                damage = max(0, WEAPONS['trap']['damage'] * (1 - distance / WEAPONS['trap']['radius']))
                enemy.take_damage(damage)
        self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = math.radians(angle)
        self.speed = 10
        
    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        if not (0 <= self.rect.x <= WINDOW_WIDTH and 0 <= self.rect.y <= WINDOW_HEIGHT):
            self.kill()
