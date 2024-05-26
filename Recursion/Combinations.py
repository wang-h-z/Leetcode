from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # k is number of pairs
        # n is range of numbers
        output, sol = [], []
        
        def generate(start): 
            if len(sol) == k: 
                output.append(sol.copy())
                print(output)
            
            else: 
                for i in range(start, n+1): 
                    sol.append(i)
                    generate(i + 1)
                    sol.pop()
        
        generate(1)
        return output