import heapq
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = []
        
        l, r = 0, k - 1
        for l in range(r + 1): 
            heap.append((-nums[l], l))
        heapq.heapify(heap)

        l, r, index = 0, k - 1, 0 
        init_max = float("inf") 
        while r < len(nums): 
            if l != 0: 
                heapq.heappush(heap, (-nums[r], r))
           
            if index < l: 
                heapq.heappop(heap)
                init_max = heap[0][0]
            new_max = heap[0][0]
            if new_max < init_max:
                init_max = new_max
                index = heap[0][1]
            
            if index <= r and index >= l:
                output.append(-init_max)
            l += 1  
            r += 1
        
        return output
            
        

print(Solution().maxSlidingWindow([1 -1], 1))

