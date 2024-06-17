from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        directions = [0, 1, 0, -1, 0]
        
        for i in range(m):
            for j in range(n): 
                if mat[i][j] == 0: 
                    queue.append((i,j))
    
        while queue: 
            i,j == queue.popleft()
            for dir in range(4): 
                new_i, new_j = i + directions[dir], j + directions[dir + 1]
                if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n or mat[new_i][new_j] == 0: 
                    continue
                else: 
                    mat[new_i][new_j] = mat[i][j] + 1
                    queue.append((new_i, new_j))
             
        return mat