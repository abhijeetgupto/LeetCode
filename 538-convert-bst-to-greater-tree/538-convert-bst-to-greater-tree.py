import bisect
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root :
            return 
        
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
        new = []
        curr = 0
        
        for num in arr :
            curr += num
            new.append(curr)
        
        stack = [root]
        while stack :
            top = stack.pop()
            idx = bisect.bisect_left(arr, top.val)
            top.val += new[-1] - new[idx]
            if top.left :
                stack.append(top.left)
            if top.right :
                stack.append(top.right)
        
        return root
            
        
        