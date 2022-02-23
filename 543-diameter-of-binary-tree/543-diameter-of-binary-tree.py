# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def rec(node = root) :
            
            if not node.left and not node.right :
                return [1,0]
            
            x1=x2=[0,0]
            if node.left :
                x1 = rec(node.left)
            
            if node.right :
                x2 = rec(node.right)
            
            return [1 + max(x1[0], x2[0]), max(1+x1[0]+x2[0], x1[1], x2[1])]
        
        
        return max(rec())-1

            
            
        