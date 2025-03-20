from enum import Enum
import random

class CellState(Enum):
    EMPTY = 0
    MISS = 1
    HIT = 2

class GameBoard:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[random.choice([CellState.EMPTY, CellState.MISS, CellState.HIT]) for _ in range(size)] for _ in range(size)]
    
    def mark_hit(self, row, col):
        self.grid[row][col] = CellState.HIT
    
    def mark_miss(self, row, col):
        self.grid[row][col] = CellState.MISS
    
    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == CellState.EMPTY
    
    def all_hits_found(self):
        return all(CellState.HIT not in row for row in self.grid)
    
    def display_board(self):
        for row in self.grid:
            print(" ".join(str(cell.value) for cell in row))

class AIPlayer:
    def __init__(self, board):
        self.board = board
        self.target_stack = []  # Stack for prioritized moves
        self.visited_moves = set()
    
    def choose_move(self):
        while self.target_stack:
            row, col = self.target_stack.pop()
            if (row, col) not in self.visited_moves and self.board.is_valid_move(row, col):
                return row, col
        
        while True:
            row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
            if (row, col) not in self.visited_moves and self.board.is_valid_move(row, col):
                return row, col
    
    def update_with_hit(self, row, col):
        self.board.mark_hit(row, col)
        self.visited_moves.add((row, col))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) not in self.visited_moves and self.board.is_valid_move(new_row, new_col):
                self.target_stack.append((new_row, new_col))
    
    def update_with_miss(self, row, col):
        self.board.mark_miss(row, col)
        self.visited_moves.add((row, col))

# Solve the board
board = GameBoard()
ai = AIPlayer(board)
print("Initial Board:")
board.display_board()
print("---")

move_count = 0
while not board.all_hits_found():
    row, col = ai.choose_move()
    print(f"AI chooses: ({row}, {col})")
    
    if board.grid[row][col] == CellState.HIT:
        print("Already a hit, continuing...")
        continue
    elif random.choice([True, False]):  # Simulate actual hits/misses
        print("Hit!")
        ai.update_with_hit(row, col)
    else:
        print("Miss!")
        ai.update_with_miss(row, col)
    
    board.display_board()
    print("---")
    move_count += 1

print(f"AI solved the board in {move_count} moves!")
