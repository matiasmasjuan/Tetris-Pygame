from parameters import *
from tetromino import Tetromino
from timer import Timer

class Game:
    def __init__(self,
                get_next_shape: callable,
                update_score: callable,
                game_over: callable, 
                update_hold_piece: callable
                ) -> None:
        
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

        self.rect = self.surface.get_rect(topleft=(2 * WINDOW_PADDING + LEFT_SIDEBAR_WIDTH, WINDOW_PADDING))
        self.sprites = pygame.sprite.Group()

        self.game_over = game_over

        self.field_matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.get_next_shape = get_next_shape
        self.tetromino = None
        self.create_new_tetromino()

        self.update_score = update_score
        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

        self.holded = False
        self.holded_shape = None
        self.update_hold_piece = update_hold_piece

        self.down_speed = 0 
        self.down_speed_faster = self.down_speed * FAST_SPEED_MULTIPLIER
        self.down_pressed = False
        self.timers = {
            'VERTICAL_MOVE' : Timer(self.down_speed, True, self.move_down),
            'HORIZONTAL_MOVE': Timer(HORIZONTAL_MOVE_WAIT_TIME),
            'HARD_DROP': Timer(HARD_DROP_WAIT_TIME),
            'ROTATE': Timer(ROTATE_WAIT_TIME),
            'HOLD': Timer(HOLD_WAIT_TIME),
        }
        self.calculate_down_speed()
        self.timers['VERTICAL_MOVE'].activate()

    def calculate_down_speed(self) -> None:
        down_speed_in_seconds = (0.8 - ((self.current_level - 1) * 0.007)) ** (self.current_level - 1)
        self.down_speed = down_speed_in_seconds * 1000
        self.down_speed_faster = self.down_speed * FAST_SPEED_MULTIPLIER
        self.timers['VERTICAL_MOVE'].duration = self.down_speed

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += 10

        if self.current_lines / 10 > self.current_level:
            self.current_level += 1
            self.calculate_down_speed()
        self.update_score(self.current_level, self.current_score, self.current_lines)

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
                self.move_horizontal(-1)
                self.timers['HORIZONTAL_MOVE'].activate()

            elif keys[pygame.K_RIGHT]:
                self.move_horizontal(1)
                self.timers['HORIZONTAL_MOVE'].activate()
        
        if not self.timers['ROTATE'].active:
            if keys[pygame.K_UP]:
                self.rotate(-90)
                self.timers['ROTATE'].activate()

            elif keys[pygame.K_LCTRL] or keys[pygame.K_z]:
                self.rotate(90)
                self.timers['ROTATE'].activate()
        
        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['VERTICAL_MOVE'].duration = self.down_speed_faster

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['VERTICAL_MOVE'].duration = self.down_speed
        
        if not self.timers['HOLD'].active and not self.holded:
            if keys[pygame.K_c] or keys[pygame.K_LSHIFT]:
                self.handle_hold_tetromino()
        
        if not self.timers['HARD_DROP'].active:
            if keys[pygame.K_SPACE]:
                while self.move_down():
                    continue
                self.timers['HARD_DROP'].activate()
        
    def handle_hold_tetromino(self) -> None:
        holded_shape = self.holded_shape
        self.holded_shape = self.tetromino.shape
        self.update_hold_piece(self.tetromino.shape)
        self.tetromino.kill()
        if not holded_shape:
            self.tetromino = None
            self.create_new_tetromino()
        else:
            self.tetromino = Tetromino(holded_shape, self.sprites, self.field_matrix)

        self.holded = True
        self.timers['HOLD'].activate()

    def create_new_tetromino(self) -> None:
        self.check_game_over()
        self.check_fininshed_rows()
        next_shape = self.get_next_shape()
        self.tetromino = Tetromino(next_shape, self.sprites, self.field_matrix)
        self.holded = False
        
    def check_game_over(self) -> None:
        if self.tetromino:
            for block in self.tetromino.blocks:
                if block.pos.y <= 0:
                    self.game_over()

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
            
            self.calculate_score(len(clear_rows))

    def move_down(self) -> bool:
        return self.tetromino.move_down(self.create_new_tetromino)
    
    def move_horizontal(self, x: int) -> None:
        self.tetromino.move_horizontal(x)
    
    def rotate(self, degrees: int) -> None:
        self.tetromino.rotate(degrees)
    
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

