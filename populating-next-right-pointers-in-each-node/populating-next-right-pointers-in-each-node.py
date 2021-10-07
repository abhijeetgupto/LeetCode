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
        while queue :
            nq = []
            for node in queue :
                if node.left :
                    nq.append(node.left)
                    nq.append(node.right)

            queue[:] = nq
            if nq:
                last = nq.pop(0)
                while nq :
                    top = nq.pop(0)
                    last.next = top
                    last = top
                
        return root
            
                
        
        