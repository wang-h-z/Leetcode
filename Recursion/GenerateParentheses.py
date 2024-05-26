from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output, sol = [], []
        
        def backtrack(open, close): 
            
            if len(sol) == 2*n: 
                output.append(''.join(sol))
                return 
            
            if open < n: # add a closing paranthesis ie -> (()
                sol.append('(')
                backtrack(open + 1, close)
                sol.pop()
            
            if open > close: 
                sol.append(')')
                backtrack(open, close + 1)
                sol.pop()
                
        backtrack(0,0)
        return output