# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []
        stack = [root]
        
        while stack :
            
            top = stack.pop()
            arr.append(top.val)
            if top.left :
                stack.append(top.left)
            if top.right :
                stack.append(top.right)
        
        arr.sort()
        return arr[k-1]
        
        
        