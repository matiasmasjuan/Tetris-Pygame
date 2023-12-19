from parameters import *

class Score:
    def __init__(self) -> None:
        self.surface = pygame.Surface((LEFT_SIDEBAR_WIDTH, SCORE_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(WINDOW_PADDING, WINDOW_PADDING))
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE['M'])

        self.level = 1
        self.score = 0
        self.lines = 0
        self.combo = 0

    def write_text(self, x:int, y: int, text: str) -> None:
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, COLORS['TEXT'])
        text_rect = text_surface.get_rect(center = (x, y))
        self.surface.blit(text_surface, text_rect)
    
    def display_text(self) -> None:
        data = [(TEXTS['LEVEL'], self.level),
                (TEXTS['SCORE'], self.score),
                (TEXTS['LINES'], self.lines),
                (TEXTS['COMBO'], self.combo)]
        for i, text in enumerate(data):
            x = self.surface.get_width() // 2
            y = self.surface.get_height() * 0.1 + i * (self.surface.get_height() // 6)
            self.write_text(x, y, text)


    def run(self) -> None:
        self.surface.fill(COLORS['SCORE_BACKGROUND'])
        self.display_text()

        self.display_surface.blit(self.surface, (WINDOW_PADDING, WINDOW_PADDING))
        pygame.draw.rect(self.display_surface, COLORS['BORDER_COLOR'], self.rect, 2, 2)
