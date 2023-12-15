from parameters import *

class Holder:
    def __init__(self) -> None:
        self.surface = pygame.Surface((LEFT_SIDEBAR_WIDTH, HOLDER_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self) -> None:
        self.display_surface.blit(self.surface, (WINDOW_PADDING, WINDOW_PADDING + SCORE_HEIGHT))
        self.surface.fill(COLORS['HOLDER_BACKGROUND'])