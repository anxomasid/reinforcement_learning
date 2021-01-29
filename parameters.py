''' Parameters '''

BOARD_LENGTH = 7
BOARD_WIDTH = 5

STATE_START = (1, 1)
STATE_WIN = (4, 6)
STATE_LOSE = (3, 2)
STATE_OBSTACLES = [(4, 3), (1, 3)]

DETERMINISTIC = True
EXPLORATION_RATE = 0.3
LEARNING_RATE = 0.3
NUMBER_ROUNDS = 10