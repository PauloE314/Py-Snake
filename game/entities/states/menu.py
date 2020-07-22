import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.game_state import BaseGameState
from game.entities.fruit import Fruit
from game.entities.wall import Wall
from game.entities.snake import Snake



class Menu(BaseGameState):
    """
    Estado de menu inicial
    """
    name = "menu"

    def main(self):
        pass           
        

    def render(self, screen):
        pass


    def events(self, event):
        pass
        

    def setup(self):
        pass