from parameters import *

class Sequence:
    def __init__(self) -> None:
        self.surface = pygame.Surface((RIGHT_SIDEBAR_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - WINDOW_PADDING, WINDOW_PADDING))

    def display_tetrominos(self, shapes: list[str]) -> None:
        for i, shape in enumerate(shapes):
            block_positions = TETROMINOS[shape]['shape']
            color = TETROMINOS[shape]['color']
            for pos in block_positions:
                x, y = pos
                x = (x + 2) * CELL_SIZE
                y = (y + 2 + (4 * i)) * CELL_SIZE
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

    def run(self, next_shapes: list[str]) -> None:
        self.surface.fill(COLORS['SEQUENCE_BACKGROUND'])
        self.display_tetrominos(next_shapes[0:3])
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, COLORS['BORDER_COLOR'], self.rect, 2, 2)
