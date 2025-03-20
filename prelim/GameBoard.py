from mainpt1 import CellState
import random
class GameBoard:
    def __init__(self,size=10):
        self.size = size
        self.grid = [[CellState.EMPTY for _ in range(size)] for _ in range(size)]

    def mark_hit(self,row,col):
        self.grid[row][col] = CellState.HIT
        
    def mark_miss(self,row,col):
        self.grid[row][col] = CellState.MISS

    def is_valid_move(self,row,col):
        #this is to make sure it is in bounds of board
        if row>=self.size or col>=self.size or row<0 or col<0:
            return False
        #this is to make sure it is doing a move on a slot that hasnt been played yet
        if self.grid[row][col] == CellState.MISS or self.grid[row][col] == CellState.HIT:
            return False
        return True
    def all_hits_found(self):
        return all(CellState.HIT not in row for row in self.grid)
    def display_board(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

   

