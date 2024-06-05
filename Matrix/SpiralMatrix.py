from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top = 0 
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        
        while left <= right and top <= bottom: 
            # part 1 of snake 
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
            
            # part 2 of snake 
            for i in range(top, bottom + 1): 
                output.append(matrix[i][right]) 
            right -= 1
            # third part of snake
            if top <= bottom: 
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
            # 4th part of snake
            if left <= right: 
                for i in range(bottom, top - 1, -1): 
                    output.append(matrix[i][left])
                left += 1
        return output