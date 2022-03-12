"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return 
        
        l1 = head
        
        dic = {}
        temp = []
        dic2 = {}
        i = 0
        
        while l1 :
            dic2[l1] = i
            i += 1
            temp.append(l1.val)
            l1 = l1.next
        
        new = Node(temp[0])
        curr = new
        dic[0] = curr
        for i in range(1, len(temp)) :
            curr.next = Node(temp[i])
            curr = curr.next
            dic[i] = curr

        curr = new
        while head :
            node = head.random
            if node :
                idx = dic2[node]
                curr.random = dic[idx]
            
            head = head.next    
            curr = curr.next
        
        return new
            
            
        
        
            
        