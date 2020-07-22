import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.game_state import BaseGameState
from game.entities.fruit import Fruit
from game.entities.wall import Wall
from game.entities.snake import Snake



class GameOver(BaseGameState):
    """
    Estado de fim de jogo
    """
    name = "game_over"

    def main(self):
        pass           
        

    def render(self, screen):
        pass


    def events(self, event):
        pass
        

    def setup(self):
        pass