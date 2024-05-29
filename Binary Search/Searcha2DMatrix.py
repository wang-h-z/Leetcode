from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l, r = 0, (m * n) - 1
        
        
        while l <= r:
            mid = l + ((r - l) // 2) 
            i = mid // n 
            j = mid % n
            
            if matrix[i][j] == target: 
                return True
            else: 
                if matrix[i][j] < target: 
                    l = mid + 1
                else: 
                    r = mid - 1

        
        return False  

Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)