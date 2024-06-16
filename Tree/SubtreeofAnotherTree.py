class Solution:
    def sub(self, node, sub): 
        if not node and not sub: 
            return True
        if not node or not sub: 
            return False
        if node.val != sub.val: 
            return False
        return self.sub(node.left, sub.left) and self.sub(node.right, sub.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        if self.sub(root, subRoot): 
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                
        
            