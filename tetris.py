from parameters import *
from sys import exit
import random

from game import Game
from score import Score
from holder import Holder
from sequence import Sequence

class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')

        self.current_shapes = self.generate_random_bag()
        self.next_shapes = self.get_next_shape()

        self.game = Game(self.get_next_shape)
        self.score = Score()
        self.holder = Holder()
        self.sequence = Sequence()

    def generate_random_bag(self) -> list[str]:
        new_shapes = list(TETROMINOS.keys())
        random.shuffle(new_shapes)
        return new_shapes

    def get_next_shape(self) -> str:
        next_shape = self.current_shapes.pop(0)
        if len(self.current_shapes) == 3:
            self.current_shapes.extend(self.generate_random_bag())
        return next_shape

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.display_surface.fill(COLORS['WINDOW_BACKGROUND'])

            self.game.run()
            self.score.run()
            self.holder.run()
            self.sequence.run(self.current_shapes)

            pygame.display.update()
