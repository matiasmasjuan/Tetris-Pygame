from parameters import *

class Score:
    def __init__(self) -> None:
        self.surface = pygame.Surface((LEFT_SIDEBAR_WIDTH, SCORE_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self) -> None:
        self.display_surface.blit(self.surface, (WINDOW_PADDING, WINDOW_PADDING))
        self.surface.fill(COLORS['SCORE_BACKGROUND'])
