# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        last = []
        queue = [root]
        while queue:
            last = []
            nq = []
            for node in queue:
                last.append(node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            queue = nq
        
        return sum(last)
            
        