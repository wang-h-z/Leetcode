class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sorted = [] 
        def inorder(node):
            if node: 
                left = inorder(node.left)
                sorted.append(node.val)
                right = inorder(node.right)
        
        inorder(root)
        for i in range(len(sorted) - 1): 
            if sorted[i] >= sorted[i + 1]: 
                return False
        return True
        