class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.head, self.tail = 0, 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.tail < self.size - 1: 
            if self.count + 1 > self.size: 
                return False
            else: 
                self.queue[self.tail + 1] = value
                self.tail += 1 
                self.count += 1
                return True
        elif self.tail == self.size - 1: 
            if self.count + 1 > self.size: 
                return False
            else: 
                self.queue[0] = value
                self.tail = 0
                self.count += 1
                return True

    def deQueue(self) -> bool:
        if not self.queue[self.head]: 
            return False
        if self.head < self.size - 1: 
            self.queue[self.head] = None
            self.head -= 1
            
            return True

    def Front(self) -> int:
        

    def Rear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()