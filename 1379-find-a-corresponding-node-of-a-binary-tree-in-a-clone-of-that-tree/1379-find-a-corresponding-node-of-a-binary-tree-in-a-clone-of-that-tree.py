class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]
        while stack:
            node = stack.pop()
            
            if node.val == target.val :
                return node
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
                