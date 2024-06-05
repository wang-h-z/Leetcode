from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mid = n // 2
        #reverse 
        for i in range(n): 
            for j in range(n): 
                if i >= mid:
                    break
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        print(matrix)
        
        #transpose
        for i in range(n): 
            for j in range(i, n): 
                if j < i: 
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]