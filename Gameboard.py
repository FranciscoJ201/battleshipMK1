from Cellstate import CellState
class GameBoard:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[CellState.EMPTY for i in range(10)] for j in range(10)]

        # another way to write the loop.
        # grid = []
        # for row_index in range(10):
        #     row = []
        #     for col_index in range(10):
        #         row.append(CellState.EMPTY)
        #     grid.append(row)
        # self.grid = grid
        
    def mark_hit(self, row, col):
        self.grid[row][col] = CellState.HIT

    def mark_miss(self, row, col):
        self.grid[row][col] = CellState.MISS

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] not in (CellState.MISS or CellState.HIT)
    
    def all_hits_found(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if(self.grid[row][col] != CellState.HIT):
                    return False
        return True
    
    def display(self):
       for row in self.grid:
            row_string = ''
            for col in row:
                row_string += str(col.value) + ' '
            print(row_string.strip())  #whitespace at end gets removed

        
