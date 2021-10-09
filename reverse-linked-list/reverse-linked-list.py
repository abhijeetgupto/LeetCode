# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        l=[]
        current=head
        
        while current:
            l.append(current.val)
            current=current.next
        
        l.reverse()
        
        current = head
        i=0
        while current:
            current.val = l[i]
            current = current.next
            i+=1
        
        return head
        