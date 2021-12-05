# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l = []
        while head :
            l.append(head.val)
            head = head.next
        
        if not l or len(l)==1 :
            return 
        
        idx = len(l)//2        
        new = ListNode(l[0])
        curr = new
        for i in range(1,len(l)):
            if i != idx :
                curr.next = ListNode(l[i])
                curr = curr.next
        return new
        
        
        