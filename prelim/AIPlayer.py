import random
class AIPlayer:
    def __init__(self,board,target_stack):
        self.board = board
        self.target_stack = []
        self.visted_moves = set()
    def choose_move(self):
        while self.target_stack:
            row, col = self.target_stack.pop()
            if self.board_is_valid_move(row,col) and (row,col) not in self.visited_moves:
                return row, col
        
        while True: 
            row, col = random.randint(0, self.board.size-1), random.randint(0, self.board.size - 1)
            if self.board.is_valid_move(row, col) and (row, col) not in self.visited_moves:
                return row, col
            
    def update_with_hit(self,row, col):
        self.board.mark_hit(row, col)
        self.visited_moves.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir, dic in directions:
            new_row, new_col = row + dir, col + dic
            if self.board.is_valid_move(new_row,new_col) and (new_row, new_col) not in self.visted_moves:
                self.target_stack.append((new_row,new_col))

    def update_with_miss(self,row, col):
        self.board.mark_miss(row,col)
        self.visited_moves.add((row,col))
    