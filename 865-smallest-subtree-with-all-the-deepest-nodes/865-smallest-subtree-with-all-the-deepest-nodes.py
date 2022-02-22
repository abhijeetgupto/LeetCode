# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def rec(node, d=0) :
            
            if not node.left and not node.right :    
                return [node, d]
            
            x1 = x2 = False
            
            if node.left :
                x1 = rec(node.left,d+1)
            
            if node.right :
                x2 = rec(node.right,d+1)
                
            if x1 and x2 :
                if x1[1] > x2[1] :
                    return x1
                elif x2[1] > x1[1] :
                    return x2
                else:
                    return [node, x1[1]]
                
            elif x1 :
                return x1
            
            elif x2 :
                return x2
        
        if not root :
            return 
        
        res = rec(root)
        return res[0]