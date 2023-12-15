from parameters import *

class Sequence:
    def __init__(self) -> None:
        self.surface = pygame.Surface((RIGHT_SIDEBAR_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self) -> None:
        self.display_surface.blit(self.surface, (
            3 * WINDOW_PADDING + GAME_WIDTH + LEFT_SIDEBAR_WIDTH,
            WINDOW_PADDING
        ))
        
        self.surface.fill(COLORS['SEQUENCE_BACKGROUND'])
        