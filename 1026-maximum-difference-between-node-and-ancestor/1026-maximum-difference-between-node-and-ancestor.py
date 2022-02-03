# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        l = []
        def rec(root, result=0) :
            
            if not root:
                return None
            
            if not root.left and not root.right :
                return [root.val, root.val, result]
            
            else:
                if root.left and root.right :
                    x1 = rec(root.right)
                    x2 = rec(root.left)
                    res = max(abs(x1[0]-root.val), abs(x2[0]-root.val),abs(x1[1]-root.val), abs(x2[1]-root.val))
                    result = max(x1[2],x2[2],res)
                    return [min(x1[0],x2[0],x1[1],x2[1],root.val), max(x1[0],x2[0],x1[1],x2[1],root.val), result]
                    
                elif root.left :
                    x1 = rec(root.left)
                    res = max(abs(x1[0]-root.val), abs(x1[1]-root.val))
                    result = max(x1[2],res)
                    return [min(x1[0],x1[1],root.val), max(x1[0],x1[1],root.val), result]
                
                elif root.right :
                    x1 = rec(root.right)
                    res = max(abs(x1[0]-root.val), abs(x1[1]-root.val))
                    result = max(x1[2],res)
                    return [min(x1[0],x1[1],root.val), max(x1[0],x1[1],root.val), result]
            
        
        x = rec(root)
        return x[2]
                
            
        
                
            
              
        