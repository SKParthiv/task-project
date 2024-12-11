import pygame
from .constants import *
from .entities.weapons import Torrent, DoubleTorrent, QuadTorrent, Trap, Wall
from .entities.mines import Mine
from .entities.enemies import Enemy
from .ui.sidebar import Sidebar

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.grid = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.weapons = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.mines = pygame.sprite.Group()
        self.gold = 10
        self.wave = 1
        self.sidebar = Sidebar(WINDOW_WIDTH - 200, 0, 200, WINDOW_HEIGHT)
        self.selected_item = None
        self.core_hp = CORE_HP
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x = x // GRID_SIZE
            grid_y = y // GRID_SIZE
            
            if self.sidebar.rect.collidepoint(x, y):
                self.selected_item = self.sidebar.get_clicked_item(x, y)
            elif self.selected_item and self.can_place(grid_x, grid_y):
                self.place_item(grid_x, grid_y)
                
    def can_place(self, grid_x, grid_y):
        return (0 <= grid_x < GRID_COLS and 
                0 <= grid_y < GRID_ROWS and 
                self.grid[grid_y][grid_x] is None)
                
    def place_item(self, grid_x, grid_y):
        cost = WEAPONS.get(self.selected_item, {}).get('cost', 0)
        if self.gold >= cost:
            if self.selected_item == 'torrent':
                weapon = Torrent(grid_x * GRID_SIZE, grid_y * GRID_SIZE)
            elif self.selected_item == 'double_torrent':
                weapon = DoubleTorrent(grid_x * GRID_SIZE, grid_y * GRID_SIZE)
            elif self.selected_item == 'quad_torrent':
                weapon = QuadTorrent(grid_x * GRID_SIZE, grid_y * GRID_SIZE)
            elif self.selected_item == 'trap':
                weapon = Trap(grid_x * GRID_SIZE, grid_y * GRID_SIZE)
            elif self.selected_item == 'wall':
                weapon = Wall(grid_x * GRID_SIZE, grid_y * GRID_SIZE)
            elif self.selected_item.startswith('mine'):
                mine = Mine(grid_x * GRID_SIZE, grid_y * GRID_SIZE, self.selected_item)
                self.mines.add(mine)
                self.grid[grid_y][grid_x] = mine
                self.gold -= cost
                return
            
            self.weapons.add(weapon)
            self.grid[grid_y][grid_x] = weapon
            self.gold -= cost
            
    def update(self):
        self.weapons.update()
        self.enemies.update()
        self.bullets.update()
        self.mines.update()
        self.check_collisions()
        self.spawn_enemies()
        
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_grid()
        self.weapons.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)
        self.mines.draw(self.screen)
        self.sidebar.draw(self.screen)
        
    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH - 200, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH - 200, y))
            
    def check_collisions(self):
        # Collision detection between bullets and enemies
        for bullet in self.bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in collided_enemies:
                enemy.take_damage(BULLET_DAMAGE)
                bullet.kill()
        
        # Collision detection between enemies and structures
        for enemy in self.enemies:
            if pygame.sprite.spritecollideany(enemy, self.weapons):
                enemy.take_damage(enemy.damage)
                self.core_hp -= enemy.damage
                enemy.kill()
        
    def spawn_enemies(self):
        # Implement enemy spawning logic based on wave number
        pass