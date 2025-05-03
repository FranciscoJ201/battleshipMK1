from Gameboard import GameBoard
from Cellstate import CellState
class AIPlayer:
    def __init__(self,board):
        self.board = board  # The real game board
        self.target_stack = []
        self.visited_moves = set()

    def choose_move(self):
       
       for i, row in enumerate(self.board.grid):
                for j, val in enumerate(row):
                    if self.board.grid[i][j] != CellState.HIT:
                        self.board.grid[i][j] = CellState.HIT
                        
                        
