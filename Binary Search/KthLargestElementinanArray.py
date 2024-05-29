from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # slightly modified quickselect algorithm 
        # split array into [greater] [equal] [less]
        # 3 way partioning
        pivot = random.choice(nums)
        greater = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        less = [x for x in nums if x < pivot]
        
        L, M = len(greater), len(equal)
        
        if k <= len(greater): 
            return self.findKthLargest(greater, k)
        elif k > L + M: 
            return self.findKthLargest(less, k - L - M)
        else :
            return equal[0]
        
        # TC: O(n), SC: O(n)
        
    import random
class Solution(object):
    # @param k & A a integer and an array
    # @return ans a integer
    def findKthLargest(self, A, k):
        return self.quickselect(0, len(A) - 1, A, len(A) - k)
        
    def quickselect(self, start, end, A, k):
        if start == end:
            return A[start]
            
        mid = self.partition(start, end, A)
        
        if mid == k:
            return A[k]
        elif mid > k:
            return self.quickselect(start, mid - 1, A, k)
        else:
            return self.quickselect(mid + 1, end, A, k)
        
    def partition(self, start, end, A):
        pivotIndex = random.randrange(start, end + 1)
        pivot = A[pivotIndex]
        A[end], A[pivotIndex] = A[pivotIndex], A[end]
        mid = start
        for i in range(start, end):
            if A[i] < pivot:
                A[mid], A[i] = A[i], A[mid]
                mid += 1
        A[mid], A[end] = A[end], A[mid]
        return mid
    
    # TC: O(n), SC: O(1)