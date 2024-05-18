from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str): #-> List[int]:
        output = []
        left, right, counter = 0, 0, 0
        table = {}
        for index, char in enumerate(p):
            table[char] = 0
        while right < len(s): 
            if s[right] in table: 
                # check if frequeny is valid   
                if counter == table.get(s[right]): 
                    table[s[right]] = table[s[right]] + 1 
                    if right - left + 1 == len(p): 
                        counter += 1
                        output.append(left) 
                        left = right + 1
                else: 
                    left = right + 1
            else: 
                left = right + 1
            
            right += 1 
        
        return output
    
print(Solution().findAnagrams("cbaebabacd", "abc"))
