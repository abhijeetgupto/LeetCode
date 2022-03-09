# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head :
            return 
        
        l = []
        while head:   
            l.append(head.val)
            head = head.next
        dic = dict(collections.Counter(l))
        l = []
        for key in dic :
            if dic[key] == 1:
                l.append(key)
        
        if not l:
            return 
        
        l.reverse()
        new = ListNode(l.pop())
        curr = new
        while l :
            curr.next = ListNode(l.pop())
            curr = curr.next
        
        return new
                
                
                
        