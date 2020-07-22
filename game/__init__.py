import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.base_game import BaseGame
from game.entities.states.playing import PlayingState
from settings import GAME_SETTINGS


class SnakeGame(BaseGame):
    """
    Jogo da cobrinha que todos amamos
    """
    states = [
        PlayingState
    ]

    initial_state = 'playing'

    def setup(self):
        # Seta o nome da aplicação
        pygame.display.set_caption("Snake")

        # Fonte do score
        score_configs = self.configs['SCORE']
        self.text_manager.new_font('score_font', score_configs['path'], score_configs['size'])
        