from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)): 
            if nums[i] <= 0 or nums[i] > len(nums): 
                nums[i] = len(nums) + 1
        
        for i in range(len(nums)): 
            curr = abs(nums[i])
            
            if curr >= len(nums) + 1: # encountered a 'useless' element 
                continue
                
            if nums[curr - 1] < 0: # duplicate, dont double count
                continue
            
            nums[curr - 1] = -1 * nums[curr - 1] # mark element with a negative number
        
        for i in range(len(nums)): 
            if nums[i] > 0: 
                return i + 1
            
        return len(nums) + 1 # case where all elements from [1...n] are in the set, return first missing positive n + 1