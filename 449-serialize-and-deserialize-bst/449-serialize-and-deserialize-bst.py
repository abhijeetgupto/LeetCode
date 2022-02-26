# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def rec(node):
            if not node :
                return ""
            else:
                return str(node.val)+"#"+rec(node.left)+"#"+rec(node.right)
        
        return rec(root)
        
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        l = data.split('#')
        preorder = []
        
        for s in l :
            if s != "" :
                preorder.append(int(s))
                
        if not preorder:
            return 
        
        root = TreeNode(preorder[0])
        curr = root
        stack = [root]
        for i in range(1,len(preorder)):
            if preorder[i] < stack[-1].val :
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            
            else:
                while stack and stack[-1].val < preorder[i] :
                    last = stack.pop()
                last.right = TreeNode(preorder[i])
                stack.append(last.right)
                               
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans