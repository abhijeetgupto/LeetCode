# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        def rec(curr = root):
            
            if not curr :
                return None
            
            if curr.val < low :
                return rec(curr.right)
                
            elif curr.val > high :
                return rec(curr.left)
            
            else:
                temp = TreeNode(curr.val)
                temp.right = rec(curr.right)
                temp.left = rec(curr.left)
                return temp
            
        return rec()
                
        
        
                    
                