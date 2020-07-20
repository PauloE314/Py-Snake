import os

WIDTH = 600
HEIGHT = 600

GAME_SETTINGS = {
    "WIDTH": HEIGHT,
    "HEIGHT": WIDTH,
    "DIMENTIONS": (WIDTH, HEIGHT),
    "FPS": 15,
    "SCORE": {
        'path': os.path.join('resources', 'fonts', '8-BIT WONDER.TTF'),
        'size': 15,
        'position': (40, 20),
        'color': (255, 255, 255)
    },
    "GAME_LIMITS": {
        "x": (100, WIDTH - 100),
        "y": (100, HEIGHT - 100)
    },
    "FRUITS": {
        'dimentions': (5, 5),
        'color': (255, 0, 0)
    },
    "WALLS": {
        'dimentions': (5, 5),
        'color': (200, 200, 200)
    },
    "SNAKE": {
        "initial_position": (255, 255),
        "initial_size": 5,
        "speed": 5,
        "dimentions": (5, 5),
        "color": (255, 255, 255)
    }
}
