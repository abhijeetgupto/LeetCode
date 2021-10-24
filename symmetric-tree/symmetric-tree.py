# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root.right and not root.left:
            return True
        if root.right and root.left :  
            return self.checker(root.right, root.left)
        else:
            return False
    
    def checker(self, root1, root2):
        
        if not root1 and not root2 :
            return True
        
        elif root1 and not root2 :
            return False
        
        elif root2 and not root1 :
            return False
        
        elif root1.val != root2.val :
            return False
        
        else:
            return self.checker(root1.right,root2.left) and  self.checker(root1.left,root2.right)
        