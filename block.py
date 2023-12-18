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
    
    def rotate(self, center_pos: pygame.Vector2, degrees: int) -> pygame.Vector2:
        return center_pos + (center_pos - self.pos).rotate(degrees)

    def check_horizontal_collide(self, new_pos_x: int, field_matrix: list[list[type['Block']]]) -> bool:
        if new_pos_x >= COLUMNS or new_pos_x < 0:
            return True
        
        return field_matrix[int(self.pos.y)][new_pos_x] != 0

    def check_vertical_collide(self, new_pos_y: int, field_matrix: list[list[type['Block']]]) -> bool:
        if new_pos_y >= ROWS or new_pos_y < 0:
            return True
        
        return new_pos_y >= 0 and field_matrix[new_pos_y][int(self.pos.x)] != 0

    def update(self) -> None:
        self.rect.topleft = self.pos * CELL_SIZE
