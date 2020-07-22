from game import SnakeGame
import pygame
from pygame.locals import *
from settings import GAME_SETTINGS

game = SnakeGame(GAME_SETTINGS)
# Inicia o jogo
game.run()