# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def rec(node) :
            
            if not node :
                return node
            
            node.left = rec(node.left)
            node.right = rec(node.right)
            
            if not node.right and not node.left :
                
                if node.val == target :
                    return None
                else:
                    return node
            
            return node
                

        
        res_node = rec(root)
        # if res_node.val == target and not res_node.right and not_node.left :
        #     return None
        return res_node
        