import os

WIDTH = 600
HEIGHT = 600
GAME_BLOCK = 10
FONT_8_BITS = os.path.join('resources', 'fonts', '8-BIT WONDER.TTF')

GAME_SETTINGS = {
    "WIDTH": HEIGHT,
    "HEIGHT": WIDTH,
    "DIMENSIONS": (WIDTH, HEIGHT),
    "APPLICATION_TITLE": "SNAKE",
    "FPS": 15,
    "BACKGROUND": (0, 0, 0),
    "FONTS": {
        "BIG_FONT": {
            "path": FONT_8_BITS,
            "name": "big_font",
            "size": 40,
        },
        "SMALL_FONT": {
            "path": FONT_8_BITS,
            "name": "small_font",
            "size": 15
        }
    },
    "TEXTS": {
        "TITLE": {
            "position": (WIDTH // 2, HEIGHT // 2 - 100),
            "color": (255, 255, 255),
            'font': 'big_font'
        },
        "SCORE": {
            "position": (40, 20),
            "color": (255, 255, 255),
            "font": "small_font"
        },
        "MAX_SCORE": {
            "position": (WIDTH - 200, 20),
            "color": (255, 255, 255),
            "font": "small_font",
            "path": os.path.join("game", "max_points.txt")
        },
        "START_GAME_MESSAGE": {
            "position": (WIDTH // 2, HEIGHT // 2),
            "color": (150, 150, 150),
            "high-color": (255, 255, 255),
            "font": "small_font"            
        },
        "GAME_OVER": {
            "position": (WIDTH // 2, HEIGHT // 2 - 100),
            "color": (255, 255, 255),
            "font": "big_font"            
        },
        "TRY_AGAIN": {
            "position": (WIDTH // 2, HEIGHT // 2),
            "color": (150, 150, 150),
            "high-color": (255, 255, 255),
            "font": "small_font"
        }
    },
    "SONGS": {
        "start_game": os.path.join('resources', 'songs', 'Start Game.wav'),
        # "add_point": "",
        # "game_over": "",
    },
    "GAME_LIMITS": {
        "x": (100, WIDTH - 100),
        "y": (100, HEIGHT - 100)
    },
    "FRUITS": {
        'dimensions': (GAME_BLOCK, GAME_BLOCK),
        'color': (255, 0, 0)
    },
    "WALLS": {
        'dimensions': (GAME_BLOCK, GAME_BLOCK),
        'color': (200, 200, 200)
    },
    "SNAKE": {
        "initial_position": (255, 255),
        "initial_size": 2,
        "speed": GAME_BLOCK,
        "dimensions": (GAME_BLOCK, GAME_BLOCK),
        "body_color": (255, 255, 255),
        "head_color": (255, 255, 100)
    },
}
