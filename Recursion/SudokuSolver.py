from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)] # create hashset for possible values
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        # populate initial board state
        for i in range(9): 
            for j in range(9): 
                if board[i][j] != ".":
                    row[i].add(int(board[i][j]))
                    col[j].add(int(board[i][j]))
                    box_id = i//3 * 3 + j//3
                    box[box_id].add(int(board[i][j]))
        
        # backtracking algorithm
        def backtrack(i,j): 
            nonlocal solved
            if i == 9: # finished all 8 rows 
               solved = True
               return 
                 
            # move left to right, before moving down (change j only until i = 8)
            new_i = i  + (j + 1) // 9 # if i am at j = 8, i should wrap around 
            new_j = (j + 1) % 9 # same as new_i, wrap around when j = 8
            
            if board[i][j] != ".": 
                backtrack(new_i, new_j)
            
            else: 
                box_id = i // 3 * 3 + j // 3
                for num in range(1,10): 
                    if num not in row[i] and num not in col[j] and num not in box[box_id]: # try a possible number 
                        row[i].add(num)
                        col[j].add(num)
                        box[box_id].add(num)
                        board[i][j] = str(num)
                        backtrack(new_i, new_j)
                        if not solved: 
                            row[i].remove(num)
                            col[j].remove(num)
                            box[box_id].remove(num)
                            board[i][j] = "."
        
        solved = False
        backtrack(0,0)
         
            
                        
            
                        
                        
                    
                    
                    
        