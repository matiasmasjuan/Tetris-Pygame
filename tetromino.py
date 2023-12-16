from parameters import *
from block import Block
class Tetromino():
    def __init__(self, shape: str, group: pygame.sprite.Group, field_matrix: list[list[Block]]) -> None:

        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.blocks = [Block(group, pygame.Vector2(pos), self.color) for pos in self.block_positions]
        self.field_matrix = field_matrix
    
    def move_horizontal_collide(self, x: int) -> bool:
        collisions = set(block.check_horizontal_collide(x, self.field_matrix) for block in self.blocks)
        return True in collisions
    
    def move_vertical_collide(self) -> bool:
        collisions = set(block.check_vertical_collide(self.field_matrix) for block in self.blocks)
        return True in collisions
    
    def move_horizontal(self, x: int) -> None:
        if not self.move_horizontal_collide(x):
            for block in self.blocks:
                block.move_horizontal(x)

    def move_down(self, create_new_tetromino: callable) -> bool:
        if not self.move_vertical_collide():
            for block in self.blocks:
                block.move_down()
            return True
        
        else:
            for block in self.blocks:
                self.field_matrix[int(block.pos.y)][int(block.pos.x)] = block
                
            create_new_tetromino()
            return False


