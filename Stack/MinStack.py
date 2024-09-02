class MinStack:
    def __init__(self):
        self.stack = []
        # store a tuple, first item contains the actual value, second item contains the minimum number up till this 'layer'
    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append((val, val))
        else: 
            prev_min = self.stack[-1][1]
            new_min = min(prev_min, val)
            self.stack.append((val, new_min))
            
    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
