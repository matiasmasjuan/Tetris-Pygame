from parameters import *
from tetromino import Tetromino
from timer import Timer
import random

class Game:
    def __init__(self) -> None:
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

        self.rect = self.surface.get_rect(topleft=(2 * WINDOW_PADDING + LEFT_SIDEBAR_WIDTH, WINDOW_PADDING))
        self.sprites = pygame.sprite.Group()

        self.field_matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.create_new_tetromino()

        self.timers = {
            'VERTICAL_MOVE' : Timer(SPEED, True, self.move_down),
            'HORIZONTAL_MOVE': Timer(HORIZONTAL_MOVE_WAIT_TIME),
            'SOFT_DROP': Timer(SOFT_DROP_WAIT_TIME)
        } 
        self.timers['VERTICAL_MOVE'].activate()

    def draw_game_grid(self) -> None:
        for column in range(1, COLUMNS):
            i = 0
            j = column * CELL_SIZE
            pygame.draw.line(self.surface, COLORS['GAME_LINE_COLOR'],
                            start_pos=(j, i), end_pos=(j, self.surface.get_height()), width=1)
        
        for row in range(1, ROWS):
            i = row * CELL_SIZE
            j = 0
            pygame.draw.line(self.surface, COLORS['GAME_LINE_COLOR'],
                            start_pos=(j, i), end_pos=(self.surface.get_width(), i), width=1)
    
    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if not self.timers['HORIZONTAL_MOVE'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['HORIZONTAL_MOVE'].activate()

            elif keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['HORIZONTAL_MOVE'].activate()
        
        if not self.timers['SOFT_DROP'].active:
            if  keys[pygame.K_DOWN]:
                self.move_down()
                self.timers['SOFT_DROP'].activate()

    def create_new_tetromino(self) -> None:
        self.check_fininshed_rows()
        self.tetromino = Tetromino(
            random.choice(list(TETROMINOS.keys())),
            self.sprites,
            self.field_matrix
        )
    
    def check_fininshed_rows(self) -> None:
        clear_rows = []
        for i, row in enumerate(self.field_matrix):
            if all(row):
                clear_rows.append(i)

        if clear_rows:
            for y in clear_rows:
                for block in self.field_matrix[y]:
                    block.kill()
            
                for row in self.field_matrix:
                    for block in row:
                        if block != 0 and block.pos.y < y:
                            block.move_down()
            
            self.field_matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
            for block in self.sprites:
                self.field_matrix[int(block.pos.y)][int(block.pos.x)] = block
            



    def move_down(self) -> None:
        self.tetromino.move_down(self.create_new_tetromino)
    
    def update_timer(self) -> None:
        for timer in self.timers.values():
            timer.update()

    def run(self) -> None:
        self.input()
        self.update_timer()
        self.sprites.update()

        self.sprites.draw(self.surface)
        self.draw_game_grid()

        self.display_surface.blit(self.surface, (2 * WINDOW_PADDING + LEFT_SIDEBAR_WIDTH, WINDOW_PADDING))
        self.surface.fill(COLORS['GAME_BACKGROUND'])

