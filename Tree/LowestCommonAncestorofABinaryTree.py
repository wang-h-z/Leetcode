class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: 
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q) 
        
        if left and right: ## p and q found, they exist in different separate subtrees
            return root
        
        if left and not right: 
            return left
        if right and not left: 
            return right
        