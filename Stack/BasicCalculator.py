class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        output = 0
        i = 0
        while i < len(s): 
            print('outer')
            char = s[i]
            if char.isdigit(): 
                sum = int(char)
                while i + 1 < len(s) and s[i + 1].isdigit(): 
                    print('inner')
                    sum = sum * 10 + int(s[i+1])
                    i += 1
                output += sum * sign
            elif char in "+-": 
                if char == "+": 
                    sign = 1  
                else: 
                    sign = -1  
            elif char == '(': 
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
                
            elif char == ')': 
                output = output * stack.pop() + stack.pop()
            i += 1    
        
        return output        
        