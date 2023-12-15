from parameters import *
from sys import exit

from game import Game
from score import Score
from holder import Holder
from sequence import Sequence

class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')

        self.game = Game()
        self.score = Score()
        self.holder = Holder()
        self.sequence = Sequence()



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
            self.sequence.run()

            pygame.display.update()
