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
        self.phase = 1 
        self.initial = 8
        self.iterate = 0
        self.neighbors = []
        self.save_move = None
        self.target_mode = False
        
