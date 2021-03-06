import pygame
from pygame.locals import *
from pygame.font import Font
from pygame.sprite import Group
from lib.game_state import BaseGameState
from lib.text_manager import Text
from game.entities.fruit import Fruit
from game.entities.wall import Wall
from game.entities.snake import Snake



class PlayingState(BaseGameState):
    """
    Estado de jogo principal
    """
    name = "playing"
    score: Text = None
    points: int = 0

    max_score: Text = None
    max_points: int = 0
    new_record: bool = False
    
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

            # Checa se há um novo score máximo
            if self.points > self.max_points:
                self.new_record = True

                # Atualiza score máximo
                self.max_score.update(text=f"MAX SCORE {self.points}")

        max_score_configs = self.configs['TEXTS']['MAX_SCORE']

        # Checa colisão com parede
        if self.snake.head.rect.collidelist(self.walls_group.sprites()) != -1:

            # Escreve novo recorde
            if self.new_record:
                with open(max_score_configs['path'], 'w') as writer:
                    writer.write(str(self.points))

            self.change_state('game_over')

        # Checa colisão consigo mesmo
        if self.snake.head.rect.collidelist(self.snake.body_rect) != -1:

            # Escreve novo recorde
            if self.new_record:
                with open(max_score_configs['path'], 'w') as writer:
                    writer.write(self.score)

            self.change_state('game_over')

            
        

    def render(self, screen):
        # Reseta tela
        screen.fill(self.configs['BACKGROUND'])

        # Renderiza o score
        self.score.render(screen)

        # Renderiza score máximo
        self.max_score.render(screen)

        # Renderiza frutinha
        self.fruit.draw(screen)

        # Renderiza muralhas
        self.walls_group.update()
        self.walls_group.draw(screen)

        # Renderiza cobra
        self.snake.draw(screen)
        self.snake.update()


    def events(self, event, screen):
        # envia os eventos para a cobra
        self.snake.events(event)
        

    def setup(self):
        self.reset()
        # Cria placar do jogador
        score_configs = self.configs['TEXTS']['SCORE']
        self.score = self.text_manager.new_text(
            text='SCORE 0',
            text_name='score',
            font_name=score_configs['font'],
            position=score_configs['position'],
            color=score_configs['color']
        )

        # Cria placar de pontuação máxima
        max_score_configs = self.configs['TEXTS']['MAX_SCORE']

        # Lê arquivo de pontuação máxima
        with open(max_score_configs['path']) as max_score_file:
            max_score = max_score_file.readline()
            max_score = int(max_score) if max_score else 0

            # Salva score máximo
            self.max_points = max_score

            # Cria o texto
            self.max_score = self.text_manager.new_text(
                text=f'MAX SCORE {max_score}',
                text_name='max_score',
                font_name=max_score_configs['font'],
                position=max_score_configs['position'],
                color=max_score_configs['color']
            )

        # Gera frutinha
        self.fruit = Fruit({**self.configs['FRUITS'], 'limits': self.configs['GAME_LIMITS']})

        # Gera muralhas
        self.walls_group = Group()
        generate_walls(self.walls_group, self.configs)

        # Gera cobrinha
        self.snake = Snake(self.configs['SNAKE'])

        # print(self.screen)

    def reset(self):
        """
        Reseta as configurações do jogo
        """
        self.points = 0
        self.fruit = None
        self.walls_group = None
        self.snake = None
        self.score = None



def generate_walls(walls_group, configs):
    """
    Gera as paredes da aplicação
    """
    wall_width, wall_heigh = configs['WALLS']['dimensions']
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