
from Gameboard import GameBoard
import random



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
# board.grid[0][1] = CellState.HIT
# print(board.all_hits_found())
board.display()

#row in range(len(self.grid))
#col in range(len(self.grid))