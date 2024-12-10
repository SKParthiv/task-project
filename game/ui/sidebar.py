import pygame
from ..constants import *

class Sidebar:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.items = [
            {'name': 'torrent', 'cost': WEAPONS['torrent']['cost']},
            {'name': 'double_torrent', 'cost': WEAPONS['double_torrent']['cost']},
            {'name': 'quad_torrent', 'cost': WEAPONS['quad_torrent']['cost']},
            {'name': 'trap', 'cost': WEAPONS['trap']['cost']},
            {'name': 'wall', 'cost': WEAPONS['wall']['cost']},
            {'name': 'ultimate', 'cost': WEAPONS['ultimate']['cost']}
        ]
        
    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)
        y = 10
        for item in self.items:
            text = f"{item['name']} ({item['cost']}G)"
            font = pygame.font.Font(None, 24)
            text_surface = font.render(text, True, BLACK)
            screen.blit(text_surface, (self.rect.x + 10, y))
            y += 40
            
    def get_clicked_item(self, x, y):
        item_height = 40
        index = (y - self.rect.y) // item_height
        if 0 <= index < len(self.items):
            return self.items[index]['name']
        return None