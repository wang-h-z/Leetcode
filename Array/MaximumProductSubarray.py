from typing import List

# O(n) time O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        result = -float('inf')
        for i in nums:
            tempMax = currMax
            currMax = max(i, currMax * i, currMin * i)
            currMin = min(tempMax * i, currMin * i, i)
            result = max(currMax, result)
        return result