from parameters import *

class HighScore:
    def __init__(self) -> None:
        self.surface = pygame.Surface((RIGHT_SIDEBAR_WIDTH, HIGHSCORE_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - WINDOW_PADDING,
                                                    WINDOW_PADDING + SEQUENCE_HEIGHT))
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE['M'])
    
    def display_text(self, highest_score: str) -> None:
        x1 = self.surface.get_width() // 2
        y1 = self.surface.get_height() // 3
        x2 = self.surface.get_width() // 2
        y2 = self.surface.get_height() // 2

        text_surface = self.font.render(TEXTS['HIGHSCORE'], True, COLORS['TEXT'])
        text_highest = self.font.render(highest_score, True, COLORS['TEXT'])
        text_surface_rect = text_surface.get_rect(center = (x1, y1))
        text_highest_rect = text_highest.get_rect(center = (x2, y2))

        self.surface.blit(text_surface, text_surface_rect)
        self.surface.blit(text_highest, text_highest_rect)
        
    def run(self, highest_score: int) -> None:
        self.surface.fill(COLORS['HOLDER_BACKGROUND'])
        self.display_text(str(highest_score))
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, COLORS['BORDER_COLOR'], self.rect, 2, 2)
