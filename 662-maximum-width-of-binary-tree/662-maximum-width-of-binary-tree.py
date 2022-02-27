# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue = [(root, 1)]
        res = 1 
        
        while queue:            
	
            if len(queue) >= 2:
                res = max(queue[-1][1] - queue[0][1] + 1, res)
                
            nq = []        
            for node,pos in queue:
                if node.left:
                    nq.append((node.left, 2*pos))
                if node.right:
                    nq.append((node.right, 2*pos + 1))    
                    
            queue = nq
            
        return res
            
            
        
        
        
        
                    
        