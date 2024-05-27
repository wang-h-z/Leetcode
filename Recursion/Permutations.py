from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output, sol = [],[]

        def backtrack(i): 
            if i == n: 
                output.append(sol[::])
                return
            
            for pos in range(i + 1): 
                sol.insert(pos, nums[i])
                backtrack(i + 1)
                sol.remove(nums[i])
                
        
        backtrack(0)
        return output
