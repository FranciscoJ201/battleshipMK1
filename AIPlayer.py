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

        
        constRow = 3
        while True:
            # row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
            #when it sinks a ship all the boxes around it become invalid (added to visited moves)
            #in addition must add code that recognizes whole ship, and total number of ships (in board generator)

            if (self.board.is_valid_move(row,col)) and ((row,col) not in self.visited_moves):
                row, col = row + 1, col + 1
                return row, col
            else:
                
                return row - constRow, col


# board = GameBoard()
# board.grid = preset_board
# board.display()
# AI = AIPlayer(board)
# # print(AI.choose_move())
# # print(len(AI.target_stack))
# AI.choose_move()



    #    for i, row in enumerate(self.board.grid):
    #             for j, val in enumerate(row):
    #                 if self.board.grid[i][j] != CellState.HIT:
    #                     self.board.grid[i][j] = CellState.HIT
                        
                        
