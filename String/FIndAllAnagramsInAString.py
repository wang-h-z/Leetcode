from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        left, right, counter = 0, 0, 0
        table = set()
        for i in p:
            table.add(i)
        while right < len(s):
            if s[right] in table: 
                table.remove(s[right])
                if counter == len(p) - 1: 
                    output.append(left)
                    counter = 0
                else : 
                    counter += 1
            else :
                left += 1
                counter == 0
            right += 1
        return output
    
print(Solution().findAnagrams("cbaebabacd", "abc"))
