from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])
        
        first_row = False
        first_col = False
        
        for i in range(row): 
            for j in range(col): 
                if matrix[i][j] == 0: 
                    if i == 0: 
                        first_row = True
                    if j == 0: 
                        first_col = True
                    
                    print(i,j)
                    matrix[0][j] = matrix[i][0] = 0
        
        for r in range(1, row): 
            for c in range(1, col): 
                matrix[r][c] == 0 if matrix[0][c] == 0 or matrix[r][0] == 0 else matrix[r][c]
        
        if first_row: 
            for cc in range(col):
                matrix[0][cc] = 0
        
        if first_col: 
            for rr in range(row): 
                matrix[rr][0] = 0
        
        
                    
        