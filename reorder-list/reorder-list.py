# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        curr = head
        while curr :
            l.append(curr.val)
            curr = curr.next
        res = []
        while l :
            res.append(l.pop(0))
            try:
                res.append(l.pop())
            except:
                pass
        
        if not res:
            return 
        head.val = res.pop(0)
        curr = head.next
        while curr  :
            curr.val = res.pop(0)
            curr = curr.next
