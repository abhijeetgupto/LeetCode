# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l = []
        while head :
            l.append(head.val)
            head = head.next
        
        new = ListNode(l.pop(0))
        curr = new
        
        i = 0
        j = 2
        x = 2
        
        while i < len(l) :
            temp = l[i:j]
            i = j
            x += 1
            j += x
            
        
            if len(temp)%2 == 0:
                for c in range(len(temp)-1,-1,-1):
                    curr.next = ListNode(temp[c])
                    curr = curr.next
                
            else:
                for c in range(len(temp)) :
                    curr.next = ListNode(temp[c])
                    curr = curr.next
                    
        return new
     
                
            
        
        