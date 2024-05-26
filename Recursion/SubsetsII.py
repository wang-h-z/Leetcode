class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output, sol = [], []
        
        n = len(nums)
        nums.sort()
        def backtrack(i): 
            if i == len(nums): 
                output.append(sol[::]) # pass by value, not reference
                return 
            
            # Include nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
            # Do not include nums[i]
            while i + 1 < n and nums[i] == nums[i+1]: 
                i += 1 # skip duplicate elements
            backtrack(i + 1)
            
        backtrack(0)
        return output
            
    