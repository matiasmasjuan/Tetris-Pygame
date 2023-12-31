from parameters import *

class Holder:
    def __init__(self) -> None:
        self.surface = pygame.Surface((LEFT_SIDEBAR_WIDTH, HOLDER_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(WINDOW_PADDING, WINDOW_PADDING + SCORE_HEIGHT))
        self.font = pygame.font.Font(FONT_PATH, GAME_FONT_SIZE)

    def display_tetromino(self, shape: str) -> None:
        color = TETROMINOS[shape]['color']
        block_positions = TETROMINOS[shape]['shape']
        for pos in block_positions:
            x, y = pos
            x = (x + 2) * CELL_SIZE
            y = (y + 3) * CELL_SIZE
            if shape in ['I', 'O']:
                x -= SEQUENCE_OFFSET_SIZE
            self.draw_block(x, y, color)

    def draw_block(self, x: int, y: int, color: str) -> None:
        line_color = COLORS['GAME_LINE_COLOR']
        pygame.draw.rect(self.surface, color, (x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.line(self.surface, line_color, start_pos=(x, y), end_pos=(x + CELL_SIZE, y), width=1)
        pygame.draw.line(self.surface, line_color, start_pos=(x, y), end_pos=(x, y + CELL_SIZE), width=1)
        pygame.draw.line(self.surface, line_color,
                        start_pos=(x + CELL_SIZE, y), end_pos=(x + CELL_SIZE, y + CELL_SIZE), width=1)
        pygame.draw.line(self.surface, line_color,
                        start_pos=(x, y + CELL_SIZE), end_pos=(x + CELL_SIZE, y + CELL_SIZE), width=1)
    
    def display_text(self) -> None:
        x = self.surface.get_width() * 0.5
        y = self.surface.get_height() * 0.15
        text_surface = self.font.render(TEXTS['HOLDER'], True, COLORS['TEXT'])
        text_rect = text_surface.get_rect(center = (x, y))
        self.surface.blit(text_surface, text_rect)
        
    def run(self, holded_piece: str | None) -> None:
        self.surface.fill(COLORS['HOLDER_BACKGROUND'])
        self.display_text()
        if holded_piece:
            self.display_tetromino(holded_piece)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, COLORS['BORDER_COLOR'], self.rect, 2, 2)
