from enum import Enum
import random

class CellState(Enum):
    EMPTY = 0
    MISS = 1
    HIT = 2
    SHIP = 3

class GameBoard:
    def __init__(self, size=10, newBoard=None):
        self.size = size
        self.grid = newBoard if newBoard is not None else [[CellState.EMPTY for _ in range(size)] for _ in range(size)]

class AIPlayer:
    def __init__(self, board):
        self.board = board  # The real game board
        self.AIBoard = GameBoard()  # AI's own tracking board
        self.target_stack = []
        self.visited_moves = set()
        
# Initialize game board with random hits/misses
preset_board = [
    [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
]

