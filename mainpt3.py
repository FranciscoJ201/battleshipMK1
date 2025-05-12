from Gameboard import GameBoard
from AIPlayer import AIPlayer
import random
from boards import preset_board
from boards import all_hit_board
from boards import all_miss_board
from Cellstate import CellState 

def generate_2d_list(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Randomly determine how many 3s to place in the grid
    num_threes = random.randint(1, rows * cols)  # Number of 3s will be at least 1

    for _ in range(num_threes):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        grid[row][col] = 3

    return grid

board = GameBoard(grid=preset_board)
board= GameBoard()
roboPlayer = AIPlayer(board)


solution = 0
while (not board.all_hits_found()):
    board.display()
    row,col = roboPlayer.choose_move()
    # print(roboPlayer.save_move)
    # print(roboPlayer.target_mode)
    if(board.grid[row][col]==CellState.SHIP.value):
        board.mark_hit(row,col)
    else:
        board.mark_miss(row,col)
    solution +=1
    print()
print(solution)
print("new change")
   
    

