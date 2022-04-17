# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
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
        new = TreeNode(arr[0])
        curr = new
        for i in range(1,len(arr)) :
            curr.right = TreeNode(arr[i])
            curr = curr.right
        
        return new
        