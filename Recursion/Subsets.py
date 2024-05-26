from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        if not nums: 
            return [[]] 
        first = nums[0]
        rest = self.subsets(nums[1:])
        
        return rest + [subset + [first] for subset in rest]
    
print(Solution().subsets([1,2,3]))