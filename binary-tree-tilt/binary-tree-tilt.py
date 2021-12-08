class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        stack=[root]
        summ=0
        if not root:
            return 0
        
        while stack:
            node = stack.pop()
            if node.left and node.right:
                node.val = abs(self.adder(node.right)-self.adder(node.left))
                stack.append(node.right)
                stack.append(node.left)
                
            elif node.left :
                node.val = abs(self.adder(node.left))
                stack.append(node.left)
            
            elif node.right :
                node.val = abs(self.adder(node.right))
                stack.append(node.right)
            else:
                node.val = 0   
            summ += node.val
        return summ
    
    def adder(self,root):
        stack = [root]
        summ = 0
        while stack:
            node = stack.pop()
            summ += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return summ