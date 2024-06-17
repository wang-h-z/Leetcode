from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j, curr): 
            if i >= 0 and j >= 0 and i < m - 1 and j < n - 1:
                if grid[i][j] == "1": 
                    grid[i][j] = curr
                    dfs(i, j + 1, curr)
                    dfs(i, j - 1, curr)
                    dfs(i + 1, j, curr)
                    dfs(i - 1, j, curr)
        
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j, res)
        
        return res
                

