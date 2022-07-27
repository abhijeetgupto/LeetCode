# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def rec(node = root):
            
            if not node:
                return 
            
            if node.left:

                temp = node.right
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                node.right = node.left
                rightmost.right = temp
                node.left = None
                
            if node.right:
                rec(node.right)
            
        rec()
        
        
#         if not root :
#             return 
        
#         def preorder(node):
            
#             if not node:
#                 return 
            
#             order.append(node.val)
#             preorder(node.left)
#             preorder(node.right)
        
#         order = []
#         preorder(root)

#         curr = root     
#         n = len(order)
#         for i in range(len(order)):
#             curr.val = order[i]
#             curr.left = None
#             if i<n-1 and not curr.right:
#                 curr.right = TreeNode(0)
#             curr = curr.right
            
#         return 
        
        
            
        