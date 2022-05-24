# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        #[sum, no_nodes, curr_res]
        def rec(node = root):
            
            if not node:
                return [0,0,0]
            
            if not node.left and not node.right:
                return [node.val, 1, 1]
            
            else:
                x = rec(node.left)
                y = rec(node.right)
                curr_sum = x[0]+y[0]+node.val
                curr_n = x[1]+y[1]+1
                curr_res = x[2]+y[2]
                
                if curr_sum//curr_n == node.val:
                    return [curr_sum, curr_n, curr_res+1]
                
                return [curr_sum, curr_n, curr_res]
        
        return rec()[2]
            
            