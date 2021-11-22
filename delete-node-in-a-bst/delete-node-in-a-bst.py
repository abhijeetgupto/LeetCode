# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def helper(arr):
            
            if not arr :
                return 
            
            else:
                m = len(arr)//2
                root = TreeNode(arr[m])
                root.left = helper(arr[ :m])
                root.right = helper(arr[m+1 :])
                return root
        
        arr = []
        if not root:
            return 
        stack = [root]
        while stack :
            top = stack.pop()
            if top.val != key :
                arr.append(top.val)
            
            if top.left :
                stack.append(top.left)
            if top.right :
                stack.append(top.right)
        arr.sort()
        return helper(arr)
        
        