from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        rotten = deque()
    
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 2: 
                    rotten.append((i, j))
                if grid[i][j] == 1: 
                    fresh += 1
        
        while rotten and fresh > 0: 
            minutes += 1
            
            for _ in range(len(rotten)): 
                x, y = rotten.popleft()
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]: 
                    
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == m or yy < 0 or yy == n: 
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2: 
                        continue
                    
                    fresh -= 1
                    
                    grid[xx][yy] = 2
                    rotten.append((xx, yy)) 
        
        return minutes if fresh == 0 else -1     
                    