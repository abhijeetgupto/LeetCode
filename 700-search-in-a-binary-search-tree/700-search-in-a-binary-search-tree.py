# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def rec(curr = root):
            
            if not curr :
                return 
            
            if curr.val == val :
                return curr
            
            if val > curr.val :
                return rec(curr.right)
            
            else:
                return rec(curr.left)
        
        return rec()
        
        
        
        