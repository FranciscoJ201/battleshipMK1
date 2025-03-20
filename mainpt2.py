from enum import Enum
import random

class CellState(Enum):
    EMPTY = 0
    MISS = 1
    HIT = 2
    SHIP = 3

class GameBoard:
    def __init__(self, size=10, newBoard=None):
        self.size = size
        self.grid = newBoard if newBoard is not None else [[CellState.EMPTY for _ in range(size)] for _ in range(size)]

    def mark_hit(self, row, col):
        self.grid[row][col] = CellState.HIT

    def mark_miss(self, row, col):
        self.grid[row][col] = CellState.MISS

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] not in (CellState.MISS, CellState.HIT)

    def all_hits_found(self):
        return all(cell != CellState.EMPTY for row in self.grid for cell in row)

    def display_board(self):
        for row in self.grid:
            print(" ".join(str(cell.value) for cell in row))
        print()

class AIPlayer:
    def __init__(self, board):
        self.board = board  # The real game board
        self.AIBoard = GameBoard()  # AI's own tracking board
        self.target_stack = []
        self.visited_moves = set()

    def choose_move(self):
        while self.target_stack:
            row, col = self.target_stack.pop()
            if self.board.is_valid_move(row, col) and (row, col) not in self.visited_moves:
                return row, col

        while True:
            row, col = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
            if self.board.is_valid_move(row, col) and (row, col) not in self.visited_moves:
                return row, col

    def update_with_hit(self, row, col):
        self.board.mark_hit(row, col)
        # self.AIBoard.mark_hit(row, col)  # Update AI's tracking board
        self.AIBoard.grid[row][col] = CellState.HIT  # Update AI's tracking board
        self.visited_moves.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.board.is_valid_move(new_row, new_col) and (new_row, new_col) not in self.visited_moves and (new_row, new_col) not in self.target_stack:
                self.target_stack.append((new_row, new_col))

    def update_with_miss(self, row, col):
        self.board.mark_miss(row, col)
        self.AIBoard.mark_miss(row, col)  # Update AI's tracking board
        self.visited_moves.add((row, col))

# Initialize game board with random hits/misses
preset_board = [
    [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
]

board = GameBoard(size=10, newBoard=[[CellState(cell) for cell in row] for row in preset_board])
roboplayer = AIPlayer(board)

print("Initial Board:")
board.display_board()
print("---")


moves = 0
while not board.all_hits_found():
    row, col = roboplayer.choose_move()
    
    print(f"The RoboPlayer chooses {row},{col}")
    

    if board.grid[row][col] == CellState.SHIP:
        print("HIT!")
        roboplayer.update_with_hit(row, col)
    else:
        print("MISS!")
        roboplayer.update_with_miss(row, col)

    
    moves += 1

print(f"AI solved the board in {moves} moves!")
board.display_board()
print("test")
roboplayer.AIBoard.display_board()
