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
        self.phase = 0 
        self.initial = 8
        self.iterate = 0
        self.neighbors = []
        self.save_move = None
        self.target_mode = False
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
    
    def target_time(self):
        #if the AI is in target mode it must find the sqaures around it
        entry = self.neighbors.pop(0)
        while entry in self.visited_moves and len(self.neighbors)>0:
            entry = self.neighbors.pop(0)
        if entry not in self.visited_moves:
            self.visited_moves.add(entry)
            self.last_move = entry
            print(f"Moved to: {self.last_move}") 
            print(self.neighbors)
            return entry


    def choose_move(self):
        #this is "phase 0" which is just the setup of the first move in the algorithm
        if (self.phase==0):
            self.visited_moves.add((8,0))
            self.last_move = (8,0)
            self.phase +=1
            return (8,0)
        #if it hits the last part of the algorithim it will randomly shoot
        if (self.last_move == (1,9)):
            #final move in algorithim is 1,9
            #this changes phase to 2 so that it knows algoritihm is done
            self.phase = 3

        if self.target_mode and len(self.neighbors) > 0:
            entry=self.target_time()
            if entry in self.left_over:
                self.left_over.remove(entry)
            return entry
        else:
            self.target_mode = False

        #if the lastmove was a hit prio surrounding area
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
                if (not self.is_valid_move(entry)) or (entry in self.visited_moves):
                    self.neighbors.remove(entry)
            for entry in self.neighbors:
                if entry not in self.visited_moves:
                    self.visited_moves.add(entry)
                    self.last_move = entry
                    print(f"Moved to: {self.last_move} (prioritized after hit)")
                    return entry
            
            
            
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
        if (row, col) in self.visited_moves:
            print(f"Warning: Repeating move {row, col}")
        else:
            self.visited_moves.add((row,col))
        print(f"Moved to: {self.last_move}")
        # print(f"visited moves: {self.visited_moves}")
        return row, col
      

