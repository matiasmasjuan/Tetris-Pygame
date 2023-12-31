import pygame
import os

ROWS = 20
COLUMNS = 10
CELL_SIZE = 40
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE

LEFT_SIDEBAR_WIDTH = CELL_SIZE * 5
RIGHT_SIDEBAR_WIDTH = CELL_SIZE * 5

LEFT_SIDEBAR_DIVIDER = 0.7
SCORE_HEIGHT = LEFT_SIDEBAR_DIVIDER * GAME_HEIGHT
HOLDER_HEIGHT = (1 - LEFT_SIDEBAR_DIVIDER) * GAME_HEIGHT

RIGHT_SIDEBAR_DIVIDER = 0.7
SEQUENCE_HEIGHT = RIGHT_SIDEBAR_DIVIDER * GAME_HEIGHT
HIGHSCORE_HEIGHT = (1 - RIGHT_SIDEBAR_DIVIDER) * GAME_HEIGHT

WINDOW_PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + LEFT_SIDEBAR_WIDTH + RIGHT_SIDEBAR_WIDTH + 4 * WINDOW_PADDING
WINDOW_HEIGHT = GAME_HEIGHT + WINDOW_PADDING * 2

BLOCK_OFFSET_POSITION = pygame.Vector2(COLUMNS // 2, 1)
SEQUENCE_OFFSET_SIZE = CELL_SIZE // 2
HORIZONTAL_MOVE_WAIT_TIME = 150
HARD_DROP_WAIT_TIME = 300
ROTATE_WAIT_TIME = 200
HOLD_WAIT_TIME = 300
FAST_SPEED_MULTIPLIER = 0.15

FONT_PATH = os.path.join('fonts', 'Russo_One.ttf')
FONT_SIZE = {'XL': 60, 'L': 30, 'M':20, 'S': 15}
GAME_FONT_SIZE = FONT_SIZE['M'] if CELL_SIZE >= 40 else FONT_SIZE['S']

MUSIC_PATH = os.path.join('sound', 'music.wav')
MUSIC_VOLUME = 0.1

SCORES = {1: 100, 2: 300, 3: 500, 4: 800}
PERFECT_SCORES = {1: 800, 2: 1200, 3: 1800, 4: 2000}
COMBO_MULTIPLIER = 55
SOFT_DROP_SCORE = 1
HARD_DROP_MULTIPLIER = 2

TEXTS = {
    'SCORE': 'Puntaje',
    'LEVEL': 'Nivel',
    'LINES': 'Filas',
    'COMBO': 'Combo',
    'SEQUENCE': 'Siguiente',
    'HOLDER': 'Almacenado',
    'HIGHSCORE': 'Puntaje más alto',
    'GAME_OVER': 'Game Over',
    'RETRY': 'Pulse (r) para volver a jugar'
}   

COLORS = {
    'WINDOW_BACKGROUND': '#526375',
    'GAME_BACKGROUND': '#12151a',
    'HOLDER_BACKGROUND': '#12151a',
    'SCORE_BACKGROUND': '#12151a',
    'SEQUENCE_BACKGROUND': '#12151a',
    'GAME_OVER_BACKGROUND': '#526375',
    'GAME_LINE_COLOR': '#666666',
    'BORDER_COLOR': '#ffffff',
    'TEXT': '#ffffff',
    'LIGHT_BLUE': '#00d9ff',
    'DARK_BLUE': '#1200b8',
    'ORANGE': '#ff8800',
    'YELLOW': '#ffff00',
    'GREEN': '#67ff26',
    'RED': '#ff2200',
    'MAGENTA': '#a000d1',
    'SHADOW': '#999999'
}

TETROMINOS = {
	'I': {'shape': [(0,0), (1,0), (2,0), (-1,0)], 'color': COLORS['LIGHT_BLUE']},
	'J': {'shape': [(0,0), (-1,0), (-1,-1), (1,0)], 'color': COLORS['DARK_BLUE']},
	'L': {'shape': [(0,0), (1,0), (1,-1), (-1,0)], 'color': COLORS['ORANGE']},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': COLORS['YELLOW']},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': COLORS['GREEN']},
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': COLORS['MAGENTA']},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': COLORS['RED']}
}
