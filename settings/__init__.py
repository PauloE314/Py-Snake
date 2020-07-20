import os

WIDTH = 600
HEIGHT = 600

GAME_SETTINGS = {
    "WIDTH": HEIGHT,
    "HEIGHT": WIDTH,
    "DIMENTIONS": (WIDTH, HEIGHT),
    "FPS": 40,
    "SCORE": {
        'path': os.path.join('resources', 'fonts', '8-BIT WONDER.TTF'),
        'size': 15,
        'position': (40, 20),
        'color': (255, 255, 255)
    }
    
}