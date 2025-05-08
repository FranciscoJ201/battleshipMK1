from Cellstate import CellState
class GameBoard:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[CellState.EMPTY.value for i in range(10)] for j in range(10)] #defaults at 10 by 10 of 0s
        self.shipsqaures = 0
    def mark_hit(self, row, col):
        self.grid[row][col] = CellState.HIT.value

    def mark_miss(self, row, col):
        self.grid[row][col] = CellState.MISS.value 

    def is_valid_move(self, row, col):
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if (0<=row<10) and (0<=col<10) and (self.grid[row][col] in (CellState.EMPTY.value,CellState.SHIP.value)): #need this weird comparison for enumerate stuff
                    return True
        return False
    

        
    
    def all_hits_found(self):
        
        # for row in self.grid:
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if(self.grid[row][col] != CellState.HIT.value):
                    return False
        return True
    
    def display(self):
        #count ship squares & check what type of board [Cells or ints] and convert
        # if isinstance(self.grid[0][0], int):
        #     for row in range(len(self.grid)):
        #         for col in range(len(self.grid)):
        #             if self.grid[row][col] == 3:
        #                 self.shipsqaures +=1
        #             self.grid[row][col] = CellState(self.grid[row][col])

        # for row in self.grid:
        #     row_string = ''
        #     for col in row:
        #         row_string += str(col) + ' '
        #     print(row_string.strip())

        for row in self.grid:
            row_string = ''
            for col in row:
                row_string += str(col) + ' '
            print(row_string.strip())  #whitespace at end gets removed

        
