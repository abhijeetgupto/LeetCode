# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}
        def rec(curr=root, take=True) :
            
            if (curr,take) in memo :
                return memo[(curr,take)]
            
            if not curr :
                return 0
            
            else:
                if take :
                    x = max(curr.val + rec(curr.left,False)+rec(curr.right,False), rec(curr.left,True) + rec(curr.right,True))
                    memo[(curr,take)] = x
                    return x
                
                else:
                    x = rec(curr.left,True) + rec(curr.right,True)
                    memo[(curr,take)] = x
                    return x
        
        return rec()
                
        