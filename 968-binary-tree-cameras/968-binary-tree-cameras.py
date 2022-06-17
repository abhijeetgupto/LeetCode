# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(node):
            
            #camera, monitor
            if not node:
                return False, True
            
            cam,mon = False,False
            c1, m1 = dfs(node.left)
            c2, m2 = dfs(node.right)
            
            if c1 or c2:
                mon = True
            
            if not m1 or not m2:
                cam = True
                mon = True
                self.res += 1
            
            return cam,mon
        
        c,m = dfs(root)
        if not m:
            self.res += 1
        
        return self.res
                
            
            
            
            
                    
            
            