# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        
        root.val = 0
        res = set()
        def helper(node):
            
            res.add(node.val)
            
            if node.right :
                node.right.val = (2*node.val) + 2
                helper(node.right)
            
            if node.left :
                node.left.val = (2*node.val) + 1
                helper(node.left)
            
        helper(root)  
        self.tree = res

    def find(self, target: int) -> bool:
        return target in self.tree
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)