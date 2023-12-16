import pygame

ROWS = 20
COLUMNS = 10
CELL_SIZE = 40
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE

LEFT_SIDEBAR_WIDTH = 200
RIGHT_SIDEBAR_WIDTH = 200

SCORE_HOLDER_DIVIDER = 0.7
SCORE_HEIGHT = SCORE_HOLDER_DIVIDER * GAME_HEIGHT
HOLDER_HEIGHT = (1 - SCORE_HOLDER_DIVIDER) * GAME_HEIGHT

WINDOW_PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + LEFT_SIDEBAR_WIDTH + RIGHT_SIDEBAR_WIDTH + 4 * WINDOW_PADDING
WINDOW_HEIGHT = GAME_HEIGHT + WINDOW_PADDING * 2

BLOCK_OFFSET_POSITION = pygame.Vector2(COLUMNS // 2, -1)

COLORS = {
    'WINDOW_BACKGROUND': '#526375',
    'GAME_BACKGROUND': '#12151a',
    'HOLDER_BACKGROUND': '#8a7073',
    'SCORE_BACKGROUND': '#708a71',
    'SEQUENCE_BACKGROUND': '#89708a',
    'GAME_LINE_COLOR': '#666666',
    'LIGHT_BLUE': '#00d9ff',
    'DARK_BLUE': '#1200b8',
    'ORANGE': '#ff8800',
    'YELLOW': '#ffff00',
    'GREEN': '#67ff26',
    'RED': '#ff2200',
    'MAGENTA': '#a000d1',
}

TETROMINOS = {
	'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': COLORS['LIGHT_BLUE']},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': COLORS['DARK_BLUE']},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': COLORS['ORANGE']},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': COLORS['YELLOW']},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': COLORS['GREEN']},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': COLORS['RED']},
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': COLORS['MAGENTA']}
}
