from Gameboard import GameBoard
from Cellstate import CellState
from boards import preset_board
import random

class AIPlayer:
    def __init__(self,board):
        self.board = board  # The real game board
        self.target_stack = [(8,0)]
        self.visited_moves = set()

    def choose_move(self):
        #MAKE IT SO THAT IT ADDS TO TARGET STACK
        while len(self.target_stack) > 0:
            row,col = self.target_stack.pop()
            if (self.board.is_valid_move(row,col)) and ((row,col) not in self.visited_moves):
                return row, col

        row = 8 
        col = 0
        initial = 8
        iterate = 0
        done = False
        while not done:
            if row<10 and col < 10:
                self.target_stack.append((row,col))
                col += 1
                row += 1
            else:
                iterate+=2
                row= initial-iterate 
                col=0 
                self.target_stack.append((row,col))
            if row == 2 and col == 10:
                done = True


# row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
#when it sinks a ship all the boxes around it become invalid (added to visited moves)
#in addition must add code that recognizes whole ship, and total number of ships (in board generator)

board = GameBoard()
board.grid = preset_board
board.display()
AI = AIPlayer(board)
# print(AI.choose_move())
# print(len(AI.target_stack))
n=0
while n<30:
    print(AI.choose_move())
    n+=1


    #    for i, row in enumerate(self.board.grid):
    #             for j, val in enumerate(row):
    #                 if self.board.grid[i][j] != CellState.HIT:
    #                     self.board.grid[i][j] = CellState.HIT
                        
                        
