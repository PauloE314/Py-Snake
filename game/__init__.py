import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.base_game import BaseGame
from game.entities.states.menu import Menu
from game.entities.states.playing import PlayingState
from game.entities.states.game_over import GameOver
from settings import GAME_SETTINGS


class SnakeGame(BaseGame):
    """
    Jogo da cobrinha que todos amamos
    """
    states = [
        Menu,
        PlayingState,
        GameOver
    ]

    initial_state = 'menu'

    def setup(self):
        # Seta o nome da aplicação
        pygame.display.set_caption("Snake")

        # Pega fontes
        fonts = list(self.configs['FONTS'].values())

        # Registrar fontes
        self.text_manager.register_fonts(fonts)