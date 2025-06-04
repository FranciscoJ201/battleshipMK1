from Gameboard import GameBoard
from Cellstate import CellState
from boards import preset_board
import random

class AIPlayer:
    def __init__(self,board):
        self.board = board  # The real game board
        self.visited_moves = set()
        self.left_over = [] 
        self.last_move = (0,0) #configures left over pieces after algorithim

        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[0])):
                if row%2 == 0 and col%2!=0:
                    self.left_over.append((row,col))
                elif row%2!=0 and col%2==0: 
                    self.left_over.append((row,col))

    def is_valid_move(self,*args):
        if len(args) == 1 and isinstance(args[0], tuple):
            x, y = args[0]
        elif len(args) == 2:
            x, y = args
        else:
            raise ValueError("is_valid_move expects either a tuple (x, y) or two integers x, y")

        if x < 0 or x >= self.board.size:
            return False
        if y < 0 or y >= self.board.size:
            return False
        return True

    def choose_move(self):
       
      