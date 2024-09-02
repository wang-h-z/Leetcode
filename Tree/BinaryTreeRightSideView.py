class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def collect(node, depth): 
            if node: 
                if depth == len(output): 
                    output.append(node.val)
                collect(node.left, depth+1)
                collect(node.right, depth+1)
        
        collect(root, 0)
        return output
                
        