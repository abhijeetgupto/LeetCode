# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return 
        
        stack = [root]
        while stack :
            top = stack.pop()
            if top.val == val :
                return top
            
            if top.right:
                stack.append(top.right)
            if top.left :
                stack.append(top.left)
        
        return 
        
        