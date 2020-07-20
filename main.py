from game import SnakeGame
import pygame
from pygame.locals import *
from settings import GAME_SETTINGS

game = SnakeGame(GAME_SETTINGS)
# Inicia o jogo
game.init()
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()

#         elif event.type == KEYDOWN:
#             if event.key == K_0:
#                 game.run()
game.run()