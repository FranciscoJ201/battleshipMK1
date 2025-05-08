from Gameboard import GameBoard
from AIPlayer import AIPlayer
import random
from boards import preset_board
from boards import all_hit_board
from boards import all_miss_board

def generate_2d_list(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Randomly determine how many 3s to place in the grid
    num_threes = random.randint(1, rows * cols)  # Number of 3s will be at least 1

    for _ in range(num_threes):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        grid[row][col] = 3

    return grid

# note FOR SHIPQUARES TO FUNCTION PROPERLY AND OTHER KEY COMPONENTS YOU MUST DISPLAY BOARD AT THE BEGINNING OF THE PROGRAM (IMMEDIATELY AFTER INSTANTIATION OF GAMEBOARD, nothing inbetween)
board = GameBoard()
board.grid = preset_board
board.display()
roboPlayer = AIPlayer(board)



# solution = 0
# print(board.is_valid_move(0,0))
while (not board.all_hits_found()):
    row,col=roboPlayer.choose_move()
    board.grid[row][col]=2
board.display()

# board = GameBoard()
# board.grid = [[0 for _ in range(10)] for _ in range(10)]
# board.display()
# AI = AIPlayer(board)
# n = 0
# while not board.all_hits_found():
    
#     row,col=AI.choose_move()
#     board.grid[row][col]=2
#     n+=1
    
# board.display()
# print(board.all_hits_found())
# print(board.all_hits_found())
                          
   

# print(f"Solution took {solution} tries")
    
















# allhits = GameBoard()
# allmiss = GameBoard()

# allhits.grid = all_hit_board
# allmiss.grid = all_miss_board


# allmiss.display()
# allhits.display()

# print(board.all_hits_found())
# print(allmiss.all_hits_found())
# print(allhits.all_hits_found())
