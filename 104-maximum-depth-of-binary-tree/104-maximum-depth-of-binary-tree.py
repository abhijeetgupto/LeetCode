# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def rec(curr) :
            
            if not curr:
                return 0
            else:
                return 1 + max(rec(curr.right), rec(curr.left))
        
        return rec(root)
        