# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        while head :
            l.append(head.val)
            head = head.next
        l.pop(-n)
        
        if not l :
            return 
        
        new = ListNode(l.pop(0))
        curr = new 
        while l :
            curr.next = ListNode(l.pop(0))
            curr = curr.next
        
        return new
        
        