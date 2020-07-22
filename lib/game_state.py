import pygame
from lib.exceptions import NextStateException, EndGameException
from lib.text_manager import TextManager

class BaseGameState:
    """
    Classe para um estado base do jogo
    """
    name: str = None
    configs: dict = None
    text_manager: TextManager = None
    

    def __init__(self, game_configs: dict, text_manager: TextManager):
        # Armazena configurações
        self.configs = game_configs
        self.text_manager = text_manager
        

    def setup(self) -> None:
        """
        Método de setup do estado do jogo
        """
        assert False, "O setup precisa ser sobrescrito"
        # Checa se o estado possui um nome
        assert name, "Todo estado precisa de um nome"


    def main(self) -> None:
        """
        Método de lógica principal do estado do jogo
        """
        assert False, "A lógica precisa ser sobrescrito"


    def events(self, event) -> None:
        """
        Event handler do estado do jogo
        """
        assert False, "O event handler precisa ser sobrescrito"


    def render(self) -> None:
        """
        Renderiza os items da tela
        """
        assert False, "O método render deve ser sobrescrito"


    def change_state(self, state_name: str):
        """
        Avança para o próximo estado do jogo
        """
        raise NextStateException(state_name)

    def close_window(self):
        """
        Termina o jogo
        """
        pygame.quit()
        raise EndGameException()
