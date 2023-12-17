from parameters import *
from block import Block
class Tetromino():
    def __init__(self, shape: str, group: pygame.sprite.Group, field_matrix: list[list[Block]]) -> None:

        self.shape = shape
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.blocks = [Block(group, pygame.Vector2(pos), self.color) for pos in self.block_positions]
        self.field_matrix = field_matrix
    
    def move_horizontal_collide(self, x: int) -> bool:
        collisions = set(block.check_horizontal_collide(int(block.pos.x + x), self.field_matrix)
                        for block in self.blocks)
        return True in collisions
    
    def move_vertical_collide(self, y: int) -> bool:
        collisions = set(block.check_vertical_collide(int(block.pos.y + y), self.field_matrix)
                        for block in self.blocks)
        return True in collisions

    def rotate_collide(self, new_pos: list[pygame.Vector2]) -> bool:
        horizontal_collisions = set(block.check_horizontal_collide(int(new_pos[i][0]), self.field_matrix)
                                    for i, block in enumerate(self.blocks))
        vertical_collisions = set(block.check_vertical_collide(int(new_pos[i][1]), self.field_matrix)
                                    for i, block in enumerate(self.blocks))
        return True in horizontal_collisions.union(vertical_collisions)
    
    def move_horizontal(self, x: int) -> None:
        if not self.move_horizontal_collide(x):
            for block in self.blocks:
                block.move_horizontal(x)

    def move_down(self, create_new_tetromino: callable) -> bool:
        if not self.move_vertical_collide(1):
            for block in self.blocks:
                block.move_down()
            return True
        
        else:
            for block in self.blocks:
                self.field_matrix[int(block.pos.y)][int(block.pos.x)] = block

            create_new_tetromino()
            return False
    
    def rotate(self, degrees: int) -> None:
        if self.shape != 'O':
            center_pos = self.blocks[0].pos
            new_block_positions = [block.rotate(center_pos, degrees) for block in self.blocks]
            if not self.rotate_collide(new_block_positions):
                for i, block in enumerate(self.blocks):
                    block.pos = new_block_positions[i]



