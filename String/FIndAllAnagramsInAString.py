from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str): #-> List[int]:
        output = []
        l = 0
        table = {}
        for index, char in enumerate(p):
            table[char] = table.get(char, 0) + 1
        
        for r in range(len(s)): 
            if s[r] in table: 
                table[s[r]] -= 1
                while table[s[r]] < 0: 
                    table[s[l]] += 1
                    l += 1
            else: 
                table[s[r]] = -1
                while table[s[r]] < 0: 
                    table[s[l]] += 1
                    l += 1
                
            if r - l + 1 == len(p): 
                output.append(l)
        
        return output
    
print(Solution().findAnagrams("cbaebabacd", "abc"))
