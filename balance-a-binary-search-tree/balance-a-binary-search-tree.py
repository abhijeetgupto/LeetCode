# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
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
        stack = [root]
        while stack :
            node = stack.pop()
            arr.append(node.val)
            if node.left :
                stack.append(node.left)
            if node.right :
                stack.append(node.right)
        
        arr.sort()
        return helper(arr)
        
        