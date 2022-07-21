# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        diff = right-left+1
        curr1 = head  
        curr2 = head
        temp = []
        for _ in range(right):
            temp.append(curr2.val)
            curr2 = curr2.next
        
        
        for _ in range(left-1):
            curr1 = curr1.next
        
        for _ in range(diff):
            curr1.val = temp.pop()
            curr1 = curr1.next
        
        return head
           
        
        
        
        
            
            
        