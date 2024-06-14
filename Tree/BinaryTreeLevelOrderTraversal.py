from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = deque()
        frontier = []
        curr_frontier = 0
        next_frontier = 0
        
        if not root: 
            return output
        
        queue.append(root)
        curr_frontier += 1
        while queue: 
            if curr_frontier == 0: 
                print('1')
                curr_frontier = next_frontier
                output.append(frontier[:])
                frontier.clear()
                next_frontier = 0
            curr = queue.popleft()
            curr_frontier -= 1
            frontier.append(curr.val)
            print(frontier)
            if curr.left: 
                queue.append(curr.left)
                next_frontier += 1
                print('2')
            if curr.right: 
                queue.append(curr.right)
                next_frontier += 1
                print('3')
        output.append(frontier[:])
        return output