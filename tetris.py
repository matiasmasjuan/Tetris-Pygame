from parameters import *
from sys import exit
import random

from game import Game
from score import Score
from holder import Holder
from sequence import Sequence
from highscore import HighScore

class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')

        self.current_shapes = self.generate_random_bag()
        self.next_shapes = self.get_next_shape()
        self.holded_piece = None
        self.highest_score = 0

        self.score = Score()
        self.holder = Holder()
        self.sequence = Sequence()
        self.highscore = HighScore()
        self.game = Game(self.get_next_shape, self.update_score, self.game_over, self.update_hold_piece)

        self.music = pygame.mixer.Sound(MUSIC_PATH)
        self.music.set_volume(MUSIC_VOLUME)
        self.music.play(-1)

        self.font_game_over = pygame.font.Font(FONT_PATH, FONT_SIZE['XL'])
        self.font_retry = pygame.font.Font(FONT_PATH, FONT_SIZE['L'])

    def generate_random_bag(self) -> list[str]:
        new_shapes = list(TETROMINOS.keys())
        random.shuffle(new_shapes)
        return new_shapes

    def get_next_shape(self) -> str:
        next_shape = self.current_shapes.pop(0)
        if len(self.current_shapes) == 3:
            self.current_shapes.extend(self.generate_random_bag())
        return next_shape
    
    def update_hold_piece(self, holded_piece: str) -> None:
        self.holded_piece = holded_piece

    def update_score(self, level: int, score: int, lines: int, combo: int) -> None:
        self.score.level = level
        self.score.score = score
        self.score.lines = lines
        self.score.combo = combo
    
    def display_game_over_text(self) -> None:
        game_over_text = self.font_game_over.render(TEXTS['GAME_OVER'], True, COLORS['TEXT'])
        retry_text = self.font_retry.render(TEXTS['RETRY'], True, COLORS['TEXT'])
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT * (2/5)))
        rery_rect = retry_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT * (3/5)))

        self.display_surface.blit(game_over_text, game_over_rect)
        self.display_surface.blit(retry_text, rery_rect)

    def game_over(self):
        self.music.stop()
        self.display_surface.fill(COLORS['GAME_OVER_BACKGROUND'])
        self.display_game_over_text()
        pygame.display.flip()

        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting_for_restart = False
        self.restart()
        
    def restart(self) -> None:
        self.current_shapes = self.generate_random_bag()
        self.next_shapes = self.get_next_shape()
        self.holded_piece = None
        if self.score.score > self.highest_score:
            self.highest_score = self.score.score

        self.game = Game(self.get_next_shape, self.update_score, self.game_over, self.update_hold_piece)
        self.score = Score()
        self.holder = Holder()
        self.sequence = Sequence()
        self.highscore = HighScore()

        self.music.play(-1)
        self.run()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.display_surface.fill(COLORS['WINDOW_BACKGROUND'])

            self.game.run()
            self.score.run()
            self.holder.run(self.holded_piece)
            self.sequence.run(self.current_shapes)
            self.highscore.run(self.highest_score)

            pygame.display.update()
