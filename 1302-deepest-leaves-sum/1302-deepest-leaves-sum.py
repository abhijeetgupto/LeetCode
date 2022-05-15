# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        queue = [root]
        while queue:
            temp = 0
            nq = []
            for node in queue:
                temp += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            queue = nq
            res = temp
        
        return res
            
        