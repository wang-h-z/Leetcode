# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def height(root: Optional[TreeNode]): 
            nonlocal balanced
            if root == None: 
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)
            
            if abs(left_height - right_height) > 1: 
                balanced = False
                return 0
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return balanced