import random
class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.table: 
            return False 
        else: 
            self.table[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.table: 
            self.table[self.list[-1]]= self.table[val]
            temp = self.list[-1]
            self.list[self.table[val]] = temp
            self.list[-1] = val
            self.list.pop()
            self.table.pop(val)
            return True
        else: 
            return False
            
    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

set = RandomizedSet()
set.insert(0)
set.insert(1)
set.remove(0)
set.insert(2)
set.remove(1)
set.getRandom()