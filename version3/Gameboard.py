from version3.Cellstate import CellState
class GameBoard:
    def __init__(self, size=10,grid=None):
        self.size = size
        self.shipsquares = 0
        self.ships = 0
        self.grid = self.createGrid(grid)
    def mark_hit(self, row, col):
        self.grid[row][col] = CellState.HIT.value
        self.shipsquares = self.shipsquares - 1
    def mark_miss(self, row, col):
        self.grid[row][col] = CellState.MISS.value 
        
    def is_valid_move(self, row, col):
        pass
    
    def all_hits_found(self):
        return self.shipsquares == 0
    
    def display(self):
        for row in self.grid:
            row_string = ''
            for col in row:
                row_string += str(col) + ' '
            print(row_string.strip())  #whitespace at end gets removed

    def createGrid(self,grid=None):
        
        if grid:
            self.grid = grid
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    if self.grid[row][col] == CellState.SHIP.value:
                        self.shipsquares += 1
            return self.grid
        return [[CellState.EMPTY.value for _ in range(10)] for _ in range(10)]
