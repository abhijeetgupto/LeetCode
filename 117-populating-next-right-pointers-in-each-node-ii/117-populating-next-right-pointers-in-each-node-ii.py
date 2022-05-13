"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return 
        
        queue = [root]
        
        while queue:
            nq = []
            for node in queue:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            
            
            for i in range(len(nq)-1):
                nq[i].next = nq[i+1]
            
            queue = nq
        
        return root
        