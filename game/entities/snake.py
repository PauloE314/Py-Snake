import pygame
from random import choice
from pygame.locals import *
from pygame.surface import Surface
from typing import List, Tuple
from lib.exceptions import SnakeOutOfAxis


class SnakeBody:
    """
    Corpo da cobra
    """
    image: Surface = None
    rect = None

    def __init__(self, configs, position, head=None):
        # Armazena o quadrado
        self.image = Surface(configs['dimensions'])
        # Configura a posição
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.image.fill(configs['body_color'])

    def __repr__(self):
        return f"<Snake Body [x: {self.rect.x}, y: {self.rect.y}]>"


class Snake:
    """
    Classe da cobra
    """
    __x_speed = 0
    __y_speed = 0
    __default_speed = 0
    configs: dict = None
    head: SnakeBody = None
    body: List[SnakeBody] = None

    def __init__(self, configs):
        # Inicia o sprite
        initial_size = configs['initial_size'] if configs['initial_size'] < 20 else 20
        dimensions = configs['dimensions']
        initial_position = (
            (configs['initial_position'][0] // dimensions[0]) * dimensions[0],
            (configs['initial_position'][1] // dimensions[1]) * dimensions[1],
        )

        self.configs = configs

        # Seta a velocidade
        self.__default_speed = configs['speed']

        # Seta direção inicial
        initial_direction = choice(("right", "left", "up", "down"))
        self.move(initial_direction)

        # Cria a cabeça da cobra
        self.head = SnakeBody(configs, initial_position, head=True)
        self.head.image.fill(configs['head_color'])

        # Cria o corpo inicial da cobra
        self.body = []
        for i in range(initial_size):
            self.increase()

    def update(self):
        # pass
        self.walk()

    def events(self, event):
        """
        Lida com os possíveis eventos que envolvam a cobra
        """
        if event.type == KEYDOWN:
            if event.key == K_d:
                self.move('right')

            elif event.key == K_w:
                self.move('up')

            elif event.key == K_a:
                self.move('left')

            elif event.key == K_s:
                self.move('down')

    def increase(self):
        """
        Aumenta o camanho da cobra
        """
        ball_width, ball_height = self.configs['dimensions']

        # Certifica que a cobra está em um dos eixos
        if self.__x_speed and self.__y_speed:
            raise SnakeOutOfAxis()

        x_diff = ball_width if self.__x_speed > 0 else (
            -ball_width if self.__x_speed < 0 else 0)
        y_diff = ball_height if self.__y_speed > 0 else (
            -ball_height if self.__y_speed < 0 else 0)

        # Cria uma nova cabeça
        new_head = SnakeBody(
            self.configs, (self.head.rect.x + x_diff, self.head.rect.y + y_diff), head=True
        )
        new_head.image.fill(self.configs['head_color'])
        # Anexa a cabeça ao corpo
        self.head.image.fill(self.configs['body_color'])
        self.body.append(self.head)
        self.head = new_head

    def set_speed(self, x: int, y: int):
        """
        Muda a velocidade da cobra
        """

        # Checa se os valores do eixo x são opostos
        if not (self.__x_speed > 0 and x < 0 or self.__x_speed < 0 and x > 0):
            self.__x_speed = x

        # Checa se os valores do eixo y são opostos
        if not (self.__y_speed > 0 and y < 0 or self.__y_speed < 0 and y > 0):
            self.__y_speed = y

    def walk(self):
        """
        Move a cobra
        """
        # Movie o corpo
        body_len = len(self.body)
        for index in range(body_len):
            # Não atualiza o ultimo corpinho dentro do ciclo
            if index + 1 != body_len:
                self.body[index].rect.x = self.body[index + 1].rect.x
                self.body[index].rect.y = self.body[index + 1].rect.y
        # Atualiza o ultimo corpinho
        self.body[-1].rect.x = self.head.rect.x
        self.body[-1].rect.y = self.head.rect.y

        # Move a cabeça
        self.head.rect.x += self.__x_speed
        self.head.rect.y += self.__y_speed

    def move(self, direction: str):
        """
        Move a cobra em uma certa direção
        """
        # Direita
        if (direction == 'right'):
            self.set_speed(x=self.__default_speed, y=0)
        # Cima
        elif (direction == 'up'):
            self.set_speed(x=0, y=-self.__default_speed)
        # Esquerda
        elif (direction == 'left'):
            self.set_speed(x=-self.__default_speed, y=0)
        # Baixo
        elif (direction == 'down'):
            self.set_speed(x=0, y=self.__default_speed)

    def draw(self, surface: Surface):
        """
        Renderiza toda a cobra na superfície
        """
        # Renderiza a cabeça
        surface.blit(self.head.image, self.head.rect)
        # # Renderiza o corpo
        for ball in reversed(self.body):
            surface.blit(ball.image, ball.rect)

    @property
    def body_rect(self):
        rect_body_list = list(map(lambda ball: ball.rect, self.body))
        return rect_body_list
