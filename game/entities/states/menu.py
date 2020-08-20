import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.game_state import BaseGameState
from lib.text_manager import Text
from game.entities.fruit import Fruit
from game.entities.wall import Wall
from game.entities.snake import Snake
import time


class Menu(BaseGameState):
    """
    Estado de menu inicial
    """
    name = "menu"
    title: Text = None
    start_game: Text = None

    def setup(self):
        # Cria o título
        title_configs = self.configs['TEXTS']['TITLE']
        self.title = self.text_manager.new_text(
            text=self.configs['APPLICATION_TITLE'],
            text_name="title",
            font_name=title_configs['font'],
            center_position=title_configs['position'],
            color=title_configs['color']
        )

        # Cria a mensagem de começar jogo
        start_message_configs = self.configs['TEXTS']['START_GAME_MESSAGE']
        self.start_game = self.text_manager.new_text(
            text="(Aperte Enter para continuar)",
            text_name="start_message",
            font_name=start_message_configs['font'],
            center_position=start_message_configs['position'],
            color=start_message_configs['color']
        )
        


    def main(self):
        pass
        

    def render(self, screen):
        # Lima a tela
        screen.fill(self.configs['BACKGROUND'])
        # Renderiza título
        self.title.render(screen)
        # Renderiza mensagem de começo de jogo
        self.start_game.render(screen)


    def events(self, event, screen):
        # Caso o usuário aperte ENTER, começa o jogo
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                # Atualiza botão de menu
                start_message_configs = self.configs['TEXTS']['START_GAME_MESSAGE']
                self.start_game.update(color=start_message_configs['high-color'])
                self.start_game.render(screen)

                # Atualiza tela
                pygame.display.update()

                # Toca a música
                self.audio_manager.play("start_game")
                
                # Espera música acabar
                time.sleep(0.5)

                # Começa o jogo
                self.change_state('playing')        
