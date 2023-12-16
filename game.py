from parameters import *
from tetromino import Tetronimo
from timer import Timer

class Game:
    def __init__(self) -> None:
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

        self.rect = self.surface.get_rect(topleft=(2 * WINDOW_PADDING + LEFT_SIDEBAR_WIDTH, WINDOW_PADDING))
        self.sprites = pygame.sprite.Group()
        self.tetromino = Tetronimo('T', self.sprites)

        self.timers = {
            'VERTICAL_MOVE' : Timer(SPEED, True, self.move_down),
            'HORIZONTAL_MOVE': Timer(HORIZONTAL_MOVE_WAIT_TIME)
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

    def move_down(self) -> None:
        self.tetromino.move_down()
    
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

