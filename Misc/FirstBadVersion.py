class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if n == 1: 
            return 1
        mid = 1 + (n - 1) // 2
       
        if isBadVersion(mid): 
            if mid == 1: 
               return 1
            return self.firstBadVersion(mid - 1) 