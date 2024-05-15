import heapq
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        queue = nums
        i = 0
        for i in range(k):
            heapq.heappush(heap, nums[i])
        
        return heap

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3).pop)

