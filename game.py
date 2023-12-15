from parameters import *

class Game:
    def __init__(self) -> None:
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self) -> None:
        self.display_surface.blit(self.surface, (2 * WINDOW_PADDING + LEFT_SIDEBAR_WIDTH, WINDOW_PADDING))
        self.surface.fill(COLORS['GAME_BACKGROUND'])

