# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current=l1
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        while current.next:
            current=current.next
        current.next = l2
        
        current=l1
        l=[]
        while current:
            l.append(current.val)
            current=current.next
        
        l.sort()
        current=l1 
        i=0
        while current:
            current.val=l[i]
            current=current.next
            i+=1
        
        return l1