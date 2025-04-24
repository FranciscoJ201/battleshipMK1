from enum import Enum
import random

class CellState(Enum):
    EMPTY = 0
    MISS = 1
    HIT = 2
    SHIP = 3

class GameBoard:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[CellState.EMPTY for i in range(10)] for j in range(10)]

        # another way to write the loop.
        # grid = []
        # for row_index in range(10):
        #     row = []
        #     for col_index in range(10):
        #         row.append(CellState.EMPTY)
        #     grid.append(row)
        # self.grid = grid
        
    def mark_hit(self, row, col):
        self.grid[row][col] = CellState.HIT
    def mark_miss(self, row, col):
        self.grid[row][col] = CellState.MISS
    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] not in (CellState.MISS, CellState.HIT)
    def all_hits_found(self):
        return all(cell != CellState.EMPTY for row in self.grid for cell in row)
    def display(self):
        for row in self.grid:
            print(" ".join(str(cell.value) for cell in row))
        print()
class AIPlayer:
    def __init__(self, board):
        self.board = board  # The real game board
        self.AIBoard = GameBoard()  # AI's own tracking board
        self.target_stack = []
        self.visited_moves = set()
    def choose_move(self):
       pass
    def update_with_hit(self, row, col):
       pass
    def update_with_miss(self, row, col):
       pass
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
board = GameBoard()
board.grid[0][0] = CellState.HIT
board.display()

    