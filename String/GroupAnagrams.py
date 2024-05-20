from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        
        for s in strs: 
            a = [0] * 26
            for char in s: 
                a[ord(char) - ord('a')] += 1
            if tuple(a) not in output: 
                output[tuple(a)] = [s]
            else:
                output[tuple(a)].append(s)
        
        return output.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        