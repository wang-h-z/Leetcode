from collections import defaultdict
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        output, sol = [], [] 
        if not digits: 
            return output
        
        n = len(digits)
        def backtrack(i=0): 
            if i == n: 
                output.append(''.join(sol))
                return
            for letter in map[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
                
                
        backtrack(0)  
        return output  
        
    

