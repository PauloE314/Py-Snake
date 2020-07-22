import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.game_state import BaseGameState
from lib.text_manager import Text
from game.entities.fruit import Fruit
from game.entities.wall import Wall
from game.entities.snake import Snake



class GameOver(BaseGameState):
    """
    Estado de fim de jogo
    """
    name = "game_over"
    game_over_text: Text = None
    try_again_text: Text = None

    def setup(self):
        # Cria o texto de game over
        game_over_configs = self.configs['TEXTS']['GAME_OVER']
        self.game_over_text = self.text_manager.new_text(
            text="Game Over",
            text_name="game_over",
            font_name=game_over_configs['font'],
            center_position=game_over_configs['position'],
            color=game_over_configs['color']
        )
        #  Cria o texto de tentar novamente
        try_again_configs = self.configs['TEXTS']['TRY_AGAIN']
        self.try_again_text = self.text_manager.new_text(
            text="(Para tentar novamente aperte ENTER)",
            text_name="try_again",
            font_name=try_again_configs['font'],
            center_position=try_again_configs['position'],
            color=try_again_configs['color']
        )


    def main(self):
        pass           
        

    def render(self, screen):
        # Limpa tela
        screen.fill(self.configs['BACKGROUND'])
        # Renderiza texto de game_over
        self.game_over_text.render(screen)
        # Renderiza texto de tentar novamente
        self.try_again_text.render(screen)

    def events(self, event):
        # Caso o usuário aperte ENTER
        if event.type == KEYDOWN:
            # Tenta novamente
            if event.key == K_RETURN:
                self.change_state('playing')
        
