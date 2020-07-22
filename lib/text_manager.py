import pygame
from pygame.font import Font
from pygame import Surface, Rect
from pygame.time import Clock
from pygame.locals import *
from typing import List
from lib.exceptions import FontNameError, FontNotFoundError


class Text:
    """
    Classe base para textos
    """
    __content: str = None
    color: tuple = None
    pygame_text_object = None
    rect = None

    def __init__(self, text: str, color: tuple, position: tuple, font: Font, center = False):
        """
        Cria um novo texto, cartucho
        """
        self.__content = text
        self.color = color
        self.font = font
        self.pygame_text_object = self.font.render(self.__content, True, self.color)
        # Posição
        self.rect: Rect = self.pygame_text_object.get_rect()

        # Centraliza
        if center:
            self.rect.center = (position[0], position[1])
        # Não centraliza
        else:
            self.rect[0] = position[0]
            self.rect[1] = position[1]

    def __str__(self):
        return self.__content

    def update(self, text: str = None, color: tuple = None, position: tuple = None):
        """
        Atualiza texto criado previamente em uma dada superfície
        """
        # Update de texto
        if text:
            self.__content = text
        # Update de cor
        if color:
            self.color = color
        # Update de posição
        if position:
            self.rect[0] = position[0]
            self.rect[1] = position[1]
        
        self.pygame_text_object = self.font.render(self.__content, True, self.color)

    def render(self, surface: Surface):
        """
        Renderiza o texto na tela
        """
        surface.blit(self.pygame_text_object, self.rect)


class TextManager:
    """
    Organizador de textos para a aplicação
    """
    fonts = {}
    texts = {}

    def add_font(self, font_name, font_path, size) -> Font:
        """
        Adiciona uma nova fonte
        """
        if self.fonts.get(font_name):
            raise FontNameError()

        # Instancia a nova fonte
        new_font = Font(font_path, size)
        self.fonts[font_name] = new_font
        return new_font

    def register_fonts(self, font_list) -> List[Font]:
        """
        Cria várias fontes dadas em lista
        """
        returning_font_list = list(
            map(lambda font_configs: self.add_font(
                font_configs['name'],
                font_configs['path'],
                font_configs['size']
            ), font_list)
        )
        return returning_font_list

    def new_text(self, text: str = None, text_name: str = None, font_name: str = None, position: tuple = None, center_position: tuple = None, color: tuple = None):
        """
        Cria um novo texto
        """
        try:
            # Cria um texto
            font: Font = self.fonts[font_name]
            if center_position:
                new_text = Text(text, color, center_position, font, center=True)
            else:
                new_text = Text(text, color, position, font)

            # Salva o texto
            self.texts[text_name] = new_text
            return new_text
        
        # Caso a fonte não exista
        except KeyError:
            raise FontNotFoundError()

    def get_text(self, text_name: str):
        """
        Retorna um texto com tal nome
        """
        return self.texts[text_name]
