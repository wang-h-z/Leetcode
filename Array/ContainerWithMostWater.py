from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = -float('inf')
        l, r = 0, len(height) - 1
        while (l < r) :
            area = min(height[l], height[r]) * (r - l)
            result = max(area, result)
            if height[l] < height[r]:
                l += 1
            else:  
                r -= 1
            
        return result
    
height = [2,3,4,5,18,17,6]
print(Solution().maxArea(height))