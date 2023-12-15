from parameters import *

class Block(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group, pos: pygame.Vector2, color: str) -> None:
        super().__init__(group)

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        self.pos = pos + BLOCK_OFFSET_POSITION
        x = self.pos.x * CELL_SIZE
        y = self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x, y))