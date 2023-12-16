from parameters import *

class Block(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group, pos: pygame.Vector2, color: str) -> None:
        super().__init__(group)

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        self.pos = pos + BLOCK_OFFSET_POSITION
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)
    
    def move_down(self) -> None:
        self.pos.y += 1
    
    def move_horizontal(self, x: int) -> None:
        self.pos.x += x
    
    def update(self) -> None:
        self.rect.topleft = self.pos * CELL_SIZE
