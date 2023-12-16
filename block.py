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

    def check_horizontal_collide(self, x: int, field_matrix) -> bool:
        new_position = self.pos.x + x
        if new_position >= COLUMNS or new_position < 0:
            return True
        
        return field_matrix[int(self.pos.y)][int(new_position)] != 0

    def check_vertical_collide(self, field_matrix: list[list[type['Block']]]) -> bool:
        new_position = self.pos.y + 1
        if new_position >= ROWS:
            return True
        
        return new_position >= 0 and field_matrix[int(new_position)][int(self.pos.x)] != 0
    
    def update(self) -> None:
        self.rect.topleft = self.pos * CELL_SIZE
