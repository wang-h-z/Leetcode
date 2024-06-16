class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder: 
            return None
        
        root = TreeNode(preorder[0])
        id = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:id + 1], inorder[:id])
        root.right = self.buildTree(preorder[id+1:], inorder[id+1:])
        return root
        