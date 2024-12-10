# Window settings
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
GRID_SIZE = 40
GRID_COLS = WINDOW_WIDTH // GRID_SIZE
GRID_ROWS = WINDOW_HEIGHT // GRID_SIZE
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Game settings
CORE_HP = 100000
BULLET_DAMAGE = 5

# Weapon costs and properties
WEAPONS = {
    'torrent': {'cost': 2, 'hp': 5, 'bullets': 1, 'fire_rate': 1},
    'double_torrent': {'cost': 4, 'hp': 25, 'bullets': 2, 'fire_rate': 1},
    'quad_torrent': {'cost': 10, 'hp': 50, 'bullets': 4, 'fire_rate': 1},
    'trap': {'cost': 3, 'hp': 1, 'damage': 50, 'radius': 10},
    'ultimate': {'cost': 100, 'radius': 100},
    'wall': {'cost': 1, 'hp': 10}
}

# Mine properties
MINES = {
    'mine1': {'cost': 10, 'interval': 10},
    'mine2': {'cost': 50, 'interval': 5},
    'mine3': {'cost': 100, 'interval': 2.5},
    'mine4': {'cost': 5000, 'interval': 1},
    'mine5': {'cost': 10000, 'interval': 0.5}
}

# Enemy properties
ENEMIES = {
    'zombie': {'damage': 1, 'speed': 10, 'hp': 5},
    'super_zombie': {'damage': 5, 'speed': 5, 'hp': 15},
    'ultra_zombie': {'damage': 10, 'speed': 2.5, 'hp': 50},
    'sub_boss': {'damage': 100, 'speed': 1, 'hp': 100},
    'boss': {'damage': 500, 'speed': 0.5, 'hp': 500},
    'hidden_boss': {'damage': 1000, 'speed': 0.25, 'hp': 1000}
}