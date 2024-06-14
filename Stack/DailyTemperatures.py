from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for id, t in enumerate(temperatures): 
            while stack and temperatures[stack[-1]] < t: 
                last = stack.pop()
                ans[last] = id - last
            stack.append(id)
        
        return ans