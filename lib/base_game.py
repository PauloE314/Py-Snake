import pygame
from typing import List, Dict, Any, Union
from pygame.font import Font
from pygame.time import Clock
from pygame.locals import *
from lib.exceptions import FontNameError, FontNotFoundError, StateDoesNotExist, NextStateException, EndGameException
from lib.text_manager import TextManager
from lib.game_state import BaseGameState

class BaseGame:
    """
    Classe base do jogo
    """
    # Estados
    states: list = []
    initial_state: str = None
    __current_state: BaseGameState = None
    __real_state_list: List[BaseGameState] = []
    # Configurações
    configs: dict = None
    __game_ended = False
    # Tela
    screen = None
    # Clock e velocidade
    clock: Clock = None
    __fps: int = None
    # Text manager
    text_manager: TextManager = None


    def __init__(self, configs):
        """
        Inicia a aplicação
        """
        # Configurações de tempo
        self.clock = Clock()
        self.__fps = configs['FPS']
        # Configuração de tela
        self.screen = pygame.display.set_mode(configs["DIMENSIONS"])
        # Salva configurações
        self.configs = configs
        # Configurações de texto
        self.text_manager = TextManager()
        # Inicia o Jogo
        pygame.init()


    def setup(self) -> Any:
        """
        Método de configurações iniciais do jogo
        """
        pass


    def run(self) -> None:
        """
        Roda o setup do jogo e o inicia
        """
        assert self.initial_state, "O estado inicial da aplicação não foi explicitado"
        pygame.init()
        # Dá o setup inicial
        self.setup()
        # Carrega os estados do jogo
        self.__real_state_list = list(
            map(lambda cls: cls(self.configs, self.text_manager), self.states)
        )
        
        # Loop do jogo
        while True:
            # Pega o estado atual
            current_state = self.get_state(self.initial_state)

            current_state.setup()

            # Executa seu ciclo de vida até que seja chamada a uma mudança de estado
            try:
                while True:
                    self.clock.tick(self.__fps)
                    # Eventos
                    for event in pygame.event.get():
                        # Saído do jogo
                        if event.type == QUIT:
                            self.end_game()
                            return
                        # Executa o event handler do estado atual
                        current_state.events(event)

                    # Função principal
                    current_state.main()

                    # Renderiza mudanças do estado atual na tela
                    current_state.render(self.screen)

                    # Atualiza o frame
                    pygame.display.update()

            # Avança para o próximo estado
            except NextStateException as next_state:
                pygame.display.update()
                # Tenta troca o estado
                self.__current_state = self.get_state(next_state)

            # Termina o jogo
            except EndGameException:
                self.end_game()
                break
                
    

    def end_game(self) -> None:
        """
        Termina o jogo
        """
        pygame.quit()

    def get_state(self, name: str) -> BaseGameState:
        """
        Retorna um estado da aplicação se este existir.

        Exceptions:
            - StateDoesNotExist  
        """
        for state in self.__real_state_list:
            # Se encontrar um estado de mesmo nome, retorna-o
            if state.name == name:
                return state
        # Caso não encontre, retorna erro
        raise StateDoesNotExist(next_state)
                
