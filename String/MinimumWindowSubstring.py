class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        map = {}
        l = 0
        res, resL = [-1, -1], float('infinity')
        
        
        for index, char in enumerate(t): 
            map[char] = map.get(char,0) + 1
            
        # find first valid char
        
        for r in range(len(s)): 
            
            pass
             
                
        return output
    
print(Solution().minWindow("ADOBECODEBANC", "ABC"))