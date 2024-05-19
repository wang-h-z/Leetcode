class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        window, map = {}, {}
        l = 0
        res, resL = [-1, -1], float('infinity')
        
        for index, char in enumerate(t): 
            map[char] = map.get(char,0) + 1
        have, need = 0, len(map)
        
        for r in range(len(s)): 
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in map and window[c] == map[c]: 
                have += 1
            
            while have == need: 
                if (r - l + 1) < resL: 
                    resL = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in map and window[s[l]] < map[s[l]]: 
                    have -= 1
                l += 1
        
        [l,r] = res
        return s[l:r+1] if resL < float('infinity') else ""
             
            
    
print(Solution().minWindow("ADOBECODEBANC", "ABC"))