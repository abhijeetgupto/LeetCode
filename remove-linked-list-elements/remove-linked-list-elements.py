# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        res = []
        while head :
            if head.val != val :
                res.append(head.val)
            head = head.next
        
        if not res:
            return 
        
        new = ListNode(res.pop(0))
        curr = new
        while res :
            curr.next = ListNode(res.pop(0))
            curr = curr.next
        
        return new
    
            
        