import pygame
from pygame.locals import *
from pygame.font import Font
from lib.BaseGame import BaseGame


class SnakeGame(BaseGame):
    """
    Jogo da cobrinha que todos amamos
    """
    points = 0

    def main(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        # Renderiza o score
        self.score.render(self.screen)

    def events(self, event):
        pass
        

    def setup(self):
        # Seta o nome da aplicação
        pygame.display.set_caption("Snake")
        # Inicia a fonte padrão da aplicação
        
        score_configs = self.configs['SCORE']
        self.text_manager.new_font('default', score_configs['path'], score_configs['size'])
        # Cria placar
        self.score = self.text_manager.new_text(
            'SCORE 0', 'score', 'default', score_configs['position'], score_configs['color']
        )