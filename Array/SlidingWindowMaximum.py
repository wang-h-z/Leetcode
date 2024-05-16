from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # maintain maximum at the head of the queue
        queue = deque() # queue will only store the index of elements in nums, queue maintains the window
        output = []
        
        for i in range(len(nums)):
            print(len(queue))
            # check that the max element is not outside of the window while the queue is !empty
            if queue and queue[0] <= i - k: 
                queue.popleft()
            
            # pop right elements in the queue that are smaller than the current element (useless elements)
            # this also maintains the largest element onto the left
            while queue: 
                if nums[queue[-1]] < nums[i]: 
                    queue.pop()
                else: 
                    break
            
            # always append 
            queue.append(i) 
            
            if i >= k - 1: 
                output.append(nums[queue[0]])
                
        
        return output

 
