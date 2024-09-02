class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -float('infinity')
        
        def helper(node):
            nonlocal result 
            if not node:
                return 0
            
            leftMax = max(helper(node.left), 0)
            rightMax = max(helper(node.right),0)
            
            result = max(result, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax)\
        
        helper(root)
        return result
            
            