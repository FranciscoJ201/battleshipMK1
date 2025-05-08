grid = [[0 for i in range(10)] for j in range(10)] 



row = 8 
col = 0
initial = 8
iterate = 0
done = False
while not done:
    if row<10 and col < 10:
        grid[row][col]=3
        col += 1
        row += 1
    else:
        iterate+=2
        row= initial-iterate 
        col=0 
        grid[row][col]=3
    if row == 2 and col == 10:
        done = True
    

for row in grid:
            row_string = ''
            for col in row:
                row_string += str(col) + ' '
            print(row_string.strip())  #whitespace at end gets removed


