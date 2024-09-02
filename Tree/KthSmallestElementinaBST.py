class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(node): 
            if node: 
                left = inorder(node.left)
                arr.append(node.val)
                right = inorder(node.right)
        inorder(root)
        return arr[k - 1]