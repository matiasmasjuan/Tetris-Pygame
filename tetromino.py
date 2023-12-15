from parameters import *
from block import Block
class Tetronimo():
    def __init__(self, shape: str, group: pygame.sprite.Group) -> None:

        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.blocks = [Block(group, pygame.Vector2(pos), self.color) for pos in self.block_positions]