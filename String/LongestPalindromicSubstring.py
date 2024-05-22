class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandPalindrome(left, right): 
            # finds the longest possible palindrome with the position between left and right as center 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1
                right += 1
            
            return s[left + 1:right]
        maxStr = ""
        for i in range(len(s)): 
            odd = expandPalindrome(i,i)
            even = expandPalindrome(i, i + 1)
            if len(odd) > len(even): 
                if len(odd) > len(maxStr): 
                    maxStr = odd 
            else: 
                if len(even) > len(maxStr): 
                    maxStr = even
        
        return maxStr

# Alternative Solution Using Manacher's algorithm
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        # turns everything to odd length case 
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
    
        
            