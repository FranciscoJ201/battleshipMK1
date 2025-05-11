grid = [[0 for i in range(10)] for j in range(10)] 


tup = (1,0)
row = 0 
col = 0
initial = 8
iterate = 0
done = False

# Fill diagonals starting from the bottom row
for start_col in range(10):
    row, col = 9, start_col
    while row < 10 and col < 10:
        grid[row][col] = 3
        row += 1
        col += 1

# Fill diagonals starting from the left column (excluding grid[9][0] to avoid double filling)
for start_row in range(8, -1, -1):
    row, col = start_row, 0
    while row < 10 and col < 10:
        grid[row][col] = 3
        row += 1
        col += 1


  


        
for row in grid:
            row_string = ''
            for col in row:
                row_string += str(col) + ' '
            print(row_string.strip())  #whitespace at end gets removed




