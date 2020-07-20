import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.BaseGame import BaseGame
from game.entities.fruit import Fruit
from game.entities.wall import Wall
from game.entities.snake import Snake
from settings import GAME_SETTINGS


class SnakeGame(BaseGame):
    """
    Jogo da cobrinha que todos amamos
    """
    points: int = 0
    fruit: Fruit = None
    walls_group: Group = None
    snake: Snake = None

    def main(self):
        # Checa a colisão da cobra e frutinha
        if self.snake.head.rect.colliderect(self.fruit.rect):
            # Cresce a cobrinha
            self.snake.increase()
            # Cria uma nova frutinha
            self.fruit = Fruit({**self.configs['FRUITS'], 'limits': self.configs['GAME_LIMITS']})
            # Adiciona os pontos
            self.points += 10
            # Atualiza o score
            self.score.update(text = f'SCORE {self.points}')

        # Checa colisão com parede
        if self.snake.head.rect.collidelist(self.walls_group.sprites()) != -1:
            self.end_game()

        # Checa colisão consigo mesmo
        if self.snake.head.rect.collidelist(self.snake.body_rects) != -1:
            self.end_game()

            
        

    def render(self):
        # Reseta tela
        self.screen.fill((0, 0, 0))
        # Renderiza o score
        self.score.render(self.screen)

        # Renderiza frutinha
        self.fruit.draw(self.screen)

        # Renderiza muralhas
        self.walls_group.update()
        self.walls_group.draw(self.screen)

        # Renderiza cobra
        self.snake.update()
        self.snake.draw(self.screen)


    def events(self, event):
        # envia os eventos para a cobra
        self.snake.events(event)
        

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

        # Gera frutinha
        self.fruit = Fruit({**self.configs['FRUITS'], 'limits': self.configs['GAME_LIMITS']})

        # Gera muralhas
        self.walls_group = Group()
        generate_walls(self.walls_group, self.configs)

        # Gera cobrinha
        self.snake = Snake(self.configs['SNAKE'])





def generate_walls(walls_group, configs):
    """
    Gera as paredes da aplicação
    """
    wall_width, wall_heigh = configs['WALLS']['dimentions']
    x_limit_begin, x_limit_end = configs['GAME_LIMITS']['x']
    y_limit_begin, y_limit_end = configs['GAME_LIMITS']['y']
    # Percorre todos os cantos possíveis
    for y in range(y_limit_begin, y_limit_end, wall_heigh):
        for x in range(x_limit_begin, x_limit_end, wall_width):
            # Cria as paredes nas bordas esquerdas e direitas
            if (y == y_limit_begin or y == y_limit_end - wall_heigh):
                walls_group.add(
                    Wall({
                        **configs['WALLS'], 'position': (x, y)
                    })
                )
            # Cria as paredes nas bordas superiores e inferiores
            elif (x == x_limit_begin or x == x_limit_end - wall_width):
                walls_group.add(
                    Wall({
                        **configs['WALLS'], 'position': (x, y)
                    })
                )