import pygame
from pygame.sprite import Sprite
from pygame import Surface
from random import randint


class Fruit:
    """
    Classe da fruta
    """
    image: Surface = None

    def __init__(self, configs: dict):        
        # Cria a imagem
        self.image = Surface(configs['dimentions'])
        self.image.fill(configs['color'])
        self.rect = self.image.get_rect()

        # Gera posição aleatória
        # x
        self.rect.x = (randint(
            configs['limits']['x'][0] + 10,
            configs['limits']['x'][1] - 10
        ) // configs['dimentions'][0]) * configs['dimentions'][0]
        # y
        self.rect.y = (randint(
            configs['limits']['y'][0] + 10,
            configs['limits']['y'][1] - 10
        ) // configs['dimentions'][1]) * configs['dimentions'][1]



    def draw(self, surface: Surface):
        """
        Renderiza a frutinha
        """
        surface.blit(self.image, self.rect)