import pygame
from pygame import Surface
from pygame.sprite import Sprite
"""
{
    "DIMENTIONS": (X, Y),
    "COLOR": (255, 255, 255),
    "POSITION": (x, y)
    "LIMITS": {
        "x": (a, b),
        "y": (c, d)
    }
}
"""

class Wall(Sprite):
    """
    Classe do muro
    """
    def __init__(self, configs: dict):
        # Inicia o sprite
        Sprite.__init__(self)

        self.image = Surface(configs['dimentions'])
        self.image.fill(configs['color'])
        # Posição
        self.rect = self.image.get_rect()
        self.rect.x = configs['position'][0]
        self.rect.y = configs['position'][1]

    def update(self):
        pass