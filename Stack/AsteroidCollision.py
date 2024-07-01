from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        
        for a in asteroids: 
            while output and output[-1] > 0 and a < 0: 
                if output[-1] + a > 0: 
                    break
                elif output[-1] + a < 0: 
                    output.pop()
                else: 
                    output.pop()
                    break
            else: 
                output.append(a)
        
        return output
        

