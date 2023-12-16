from parameters import *
from block import Block
class Tetronimo():
    def __init__(self, shape: str, group: pygame.sprite.Group) -> None:

        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.blocks = [Block(group, pygame.Vector2(pos), self.color) for pos in self.block_positions]
    
    def move_horizontal_collide(self, x: int) -> bool:
        collisions = set(block.check_horizontal_collide(x) for block in self.blocks)
        return True in collisions
    
    def move_vertical_collide(self) -> bool:
        collisions = set(block.check_vertical_collide() for block in self.blocks)
        return True in collisions
    
    def move_horizontal(self, x: int) -> None:
        if not self.move_horizontal_collide(x):
            for block in self.blocks:
                block.move_horizontal(x)

    def move_down(self) -> None:
        if not self.move_vertical_collide():
            for block in self.blocks:
                block.move_down()
