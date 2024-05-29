from typing import List
import heapq
# Solution 1 --> 'brute force' using maxheap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        n = len(matrix)
        for i in range(n): 
            for j in range(n): 
                heapq.heappush(maxHeap, -matrix[i][j])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)
#Time Complexity -> O(N*N*logK), Space Complexity -> O(k)

# Solution 2 --> utilising minheap and sorted property and restricting to only K insertions 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        n = min(k, len(matrix)) # if k < number of rows, then its safe to say that the [k+1,number of rows] can be ignored, 
                                # since columns are also in sorted order (first index of each row is sorted)
        for r in range(n): # populate the heap with the first of values
            heapq.heappush(minHeap, (matrix[r][0], r, 0))
        ans = -1
        for i in range(k): 
            ans,r,c = heapq.heappop(minHeap)
            if c + 1 < len(matrix): # sometimes len(heap) might be < k, but it is never > k
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1)) # add the next element in the minimum element's row
        return ans
# Time Complexity -> O(K * logK + M * logK) but since M < K  usually, O(K * logK), Space Complexity -> O(k)

# Solution 3 --> binary search 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = -1
        n = len(matrix)
        def lessthanorEqual(num): 
            c = n - 1 # column counter 
            count = 0
            for r in range(n): 
                while c >= 0 and matrix[r][c] > num: 
                    c -= 1
                count += (c+1)
            return count 
        
        left, right = matrix[0][0], matrix[-1][-1]
        
        while (left < right): 
            mid = left + ((right - left) // 2)
            
            if lessthanorEqual(mid) >= k:
                ans = mid 
                right = mid 
            else: 
                left = mid + 1
        
        return ans
# Time Complexity: O((N + N) * logD), N+N time complexity for counting in lessthanorEqual, D is the difference between maxMatrixNum
# and minMatrixNum
# Space Complexity: O(1), in place! 
                    

    
    
    