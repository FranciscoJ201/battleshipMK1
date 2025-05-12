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
        
        
        #MAKE SURE TO REMOVE HITS FROM LEFT OVER ARRAY
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid[0])):
                if row%2 == 0 and col%2!=0:
                    self.left_over.append((row,col))
                elif row%2!=0 and col%2==0: 
                    self.left_over.append((row,col))

    def choose_move(self):
        
        if ((8,0) not in self.visited_moves):
            #first move in algoritihm is 8,0
            self.visited_moves.add((8,0))
            self.last_move = (8,0)
            
            return (8,0)
        
        if (self.last_move == (1,9)):
            #final move in algorithim is 1,9
            #this changes phase to 2 so that it knows algoritihm is done
            self.phase = 3

        if self.target_mode and len(self.neighbors)>0:
            row, col = self.neighbors.pop(0)
            while (row, col) in self.visited_moves and len(self.neighbors)>0:
                row, col = self.neighbors.pop(0)
            if (row, col) not in self.visited_moves:
                self.visited_moves.add((row,col))
                self.last_move = (row, col)
                print(f"Moved to: {self.last_move}") 
                print(self.neighbors)
                return row,col
        else:
            self.target_mode = False

        if (self.board.grid[self.last_move[0]][self.last_move[1]] == CellState.HIT.value):
            if not self.target_mode:
                self.save_move = self.last_move
            self.target_mode = True
            self.neighbors = [
            (self.last_move[0]-1, self.last_move[1]),  # Up
            (self.last_move[0]+1, self.last_move[1]),  # Down
            (self.last_move[0], self.last_move[1]-1),  # Left
            (self.last_move[0], self.last_move[1]+1)   # Right
            ]
            for entry in self.neighbors:
                row1, col1 = entry
                if (row1>9 or row1<0) or (col1>9 or col1 <0):
                    self.neighbors.remove(entry)
            for row, col in self.neighbors:
                if (0 <= row < len(self.board.grid)) and (0 <= col < len(self.board.grid[0])):
                    if (row, col) not in self.visited_moves:
                        self.visited_moves.add((row, col))
                        self.last_move = (row, col)
                        print(f"Moved to: {self.last_move} (prioritized after hit)")
                        return (row, col)
            
            # pass # if the grid[lastmove]= HIT: prio move
            
        elif(self.phase == 1):
            if not self.save_move == None:
                row,col = self.save_move
                self.save_move = None
            else:
                row,col = self.last_move
            
            if (row>=0 and row<9) and (col>=0 and col<9):
                col += 1
                row += 1
            else:
                self.iterate += 2
                if self.iterate > self.initial:
                    # phase 1 done
                    self.phase = 2
                    self.iterate = 9
                    self.initial = 9
                    row = 0
                    col = 0
                else:
                    row = self.initial - self.iterate 
                    col = 0

        elif(self.phase ==2):
            row,col = self.last_move
            if (row>=0 and row<9) and (col>=0 and col<9):
                col += 1
                row += 1
            else:
                self.iterate-=2
                row= 0
                col= self.initial-self.iterate 

        elif(self.phase==3):
            random_point = random.choice(self.left_over)
            self.left_over.remove(random_point)#shortens list so that it cannot possibly do same move
            row,col = random_point

        #code that should be done regardless of move type
        self.last_move = row,col
        self.visited_moves.add((row,col))
        print(f"Moved to: {self.last_move}")
        # print(f"visited moves: {self.visited_moves}")
        return row, col
      
#when it sinks a ship all the boxes around it become invalid (added to visited moves)
#in addition must add code that recognizes whole ship, and total number of ships (in board generator)

