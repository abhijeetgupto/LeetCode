# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        l = []
        while head :
            l.append(head.val)
            head = head.next
        if not l :
            return 
        k = k%len(l)
        if k != 0 :
            l = l[-k:]+l[:-k] 
        
        
        new = ListNode(l.pop(0))
        curr = new
        while l :
            curr.next = ListNode(l.pop(0))
            curr = curr.next
        return new