# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        lst = []
        
        def inorder(node = root) :
            if not node :
                return 
            
            inorder(node.left)
            lst.append(node)
            inorder(node.right)
            return
        
        inorder()
        temp = sorted([node.val for node in lst])
        for i in range(len(lst)) :
            lst[i].val = temp[i]
        
        return 
        
        
            
        
        
            
            
        
        
        
        
        
            
        
            