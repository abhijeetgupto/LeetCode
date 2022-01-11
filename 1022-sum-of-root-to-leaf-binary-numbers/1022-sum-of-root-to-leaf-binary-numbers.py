# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        l = []
        def rec(node, curr="") :
            
            if not node.left and not node.right :
                l.append(curr+str(node.val))
                return 
            
            if node.left :
                rec(node.left, curr+str(node.val))
            
            if node.right :
                rec(node.right, curr +str(node.val))
                
        rec(root)
        count = 0
        for num in l :
            count += int(num,2)
        return count
            
                
        