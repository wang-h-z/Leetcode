"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        start = node
        stack = [start]
        map = {}
        visited = []
        
        visited.append(start)
        
        while stack: 
            curr = stack.pop()
            map[curr] = Node(val=curr.val)
            visited.append(curr)
            
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        for old, new in map.items(): 
            for neighbor in old.neighbors: 
                new_neighbor = map[neighbor]
                new.neighbors.append(new_neighbor)
                
        return map[start]
            