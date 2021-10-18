# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        queue = [root]
        
        while queue:
            
            nq = []
            res = []
            
            for node in queue :
                if node.left:
                    res.append([node.val,node.left.val])
                    nq.append(node.left)
                
                if node.right:
                    res.append([node.val,node.right.val])
                    nq.append(node.right)
            
            parent_x = None
            parent_y = None
            
            for l in res :
                if l[1] == x :
                    parent_x = l[0]
                if l[1] == y :
                    parent_y = l[0]
                if parent_x and parent_y :
                    if parent_x==parent_y:
                        return False
                    else:
                        return True
            queue = nq

        return False
                
                    
                
                
                
                    
                
                    
                    
                
        
        
        