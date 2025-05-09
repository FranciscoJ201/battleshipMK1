from Cellstate import CellState
class GameBoard:
    def __init__(self, size=10,grid=None):
        self.size = size
        self.shipsquares = 0
        self.ships = 0
        self.grid = self.createGrid(grid)
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
        for row in self.grid:
            row_string = ''
            for col in row:
                row_string += str(col) + ' '
            print(row_string.strip())  #whitespace at end gets removed
    def createGrid(self,grid=None):
        print("works")
        if grid:
            self.grid = grid
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    if self.grid[row][col] == CellState.SHIP.value:
                        self.shipsquares += 1
            return self.grid
        return [[CellState.EMPTY.value for _ in range(10)] for _ in range(10)]
