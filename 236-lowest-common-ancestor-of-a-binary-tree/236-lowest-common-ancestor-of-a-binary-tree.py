# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(node):
            
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = rec(node.left)
            right = rec(node.right)
            
            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right
            
        
        return rec(root)
            
            
            
            
                
        
        