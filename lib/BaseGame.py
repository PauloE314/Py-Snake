import pygame
from pygame.time import Clock
from pygame.locals import *


class BaseGame:
    """
    Classe base do jogo
    """
    configs = None
    screen = None
    clock = None
    __fps = None
    font = None

    def __init__(self, configs):
        # Configurações de tempo
        self.clock = Clock()
        self.__fps = configs['FPS']
        self.screen = pygame.display.set_mode(configs["DIMENTIONS"])
        self.configs = configs

    def setup(self):
        """
        Método de setup do jogo
        """
        assert False, "Todo jogo precisa de um setup"

    def main(self):
        """
        Método de lógica do jogo
        """
        assert False, "A lógica precisa ser sobrescrita"

    def events(self, event):
        """
        Event handler do projeto
        """
        assert False, "O event handler precisa ser sobrescrita"

    def render(self):
        """
        Renderiza os items da tela
        """
        pass

    def run(self):
        pygame.init()
        """
        Roda o setup do jogo e o inicia
        """
        self.setup()

        # Loop do jogo
        while True:
            self.clock.tick(self.__fps)
            # Checa os eventos
            for event in pygame.event.get():
                # Sai do jogo
                if event.type == QUIT:
                    pygame.quit()
                    return
                # Event handler
                self.events(event)

            # Função principal
            self.main()

            # Renderiza coisas da tela
            self.render()
            # Atualiza a tela
            pygame.display.update()
