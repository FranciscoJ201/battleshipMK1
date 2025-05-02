
from collections import deque 
from enum import Enum
import random

class CellState(Enum):
    EMPTY = 0
    MISS = 1
    HIT = 2
class GameBoard:
    def __init__(self,size=10,newBoard = None):
        self.size = size
        if newBoard != None:
            self.grid = newBoard
        else:
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
        for row in self.grid:
            for cell in row:
                if cell != CellState.HIT:
                    return False
        return True
    def display_board(self):
        for row in self.grid:
            print(" ".join(str(cell.value) for cell in row))

   

class AIPlayer:
    def __init__(self,board,AIBoard):
        self.board = board
        self.AIBoard = AIBoard
        self.target_stack = []
        self.visited_moves = set()
    def choose_move(self):
        while self.target_stack:
            row, col = self.target_stack.pop()
            if self.board.is_valid_move(row,col) and (row,col) not in self.visited_moves:
                return row, col
        
        while True: 
            row, col = random.randint(0, self.board.size-1), random.randint(0, self.board.size - 1)
            if self.board.is_valid_move(row, col) and (row, col) not in self.visited_moves:
                return row, col
            
    def update_with_hit(self,row, col):
        self.board.mark_hit(row, col)
        self.visited_moves.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir, dic in directions:
            new_row, new_col = row + dir, col + dic
            if self.board.is_valid_move(new_row, new_col) and (new_row, new_col) not in self.visited_moves and (new_row, new_col) not in self.target_stack:
                self.target_stack.append((new_row,new_col))

    def update_with_miss(self,row, col):
        self.board.mark_miss(row,col)
        self.visited_moves.add((row,col))



new_board = [[random.choice([CellState.EMPTY, CellState.MISS, CellState.HIT]) for _ in range(10)] for _ in range(10)]
board = GameBoard(size=10,newBoard=new_board)
roboplayer = AIPlayer(board)
print("Initial Board:")
board.display_board()
print("---")

moves = 0
while not board.all_hits_found():
    row,col = roboplayer.choose_move()
    print(f"The RoboPlayer chooses {row},{col}")
    if board.grid[row][col] == CellState.HIT:
        print("HIT!")
        roboplayer.update_with_hit(row, col)
        continue
    else:
        print("MISS!")
        roboplayer.update_with_miss(row, col)
        

    board.display_board()
    print("---")
    moves += 1

print(f"AI solved the board in {moves} moves!")    
