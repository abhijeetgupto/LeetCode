# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return 
        
        if root1:
            v1 = root1.val
        else:
            v1 = 0
        
        if root2:
            v2 = root2.val
        else:
            v2 = 0
        
        root = TreeNode(v1+v2)
        if root1 and root2 :
            root.right = self.mergeTrees(root1.right,root2.right)
            root.left = self.mergeTrees(root1.left,root2.left)
        elif root1 and not root2 :
            root.right = self.mergeTrees(root1.right,None)
            root.left = self.mergeTrees(root1.left,None)
        elif not root1 and root2 :
            root.right = self.mergeTrees(None,root2.right)
            root.left = self.mergeTrees(None,root2.left)
        
        return root
            
            