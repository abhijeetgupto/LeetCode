# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n1 = 0
        curr = head
        val1 = None
        

        while curr :
            
            n1+=1
            if n1==k :
                val1 = curr.val
            
            curr = curr.next
        
        temp = None
        curr = head
        val2 = None
        
        n2 = n1-k+1
        n = 0
        
        while curr :
            
            n += 1
            if n==n2 :
                val2 = curr.val
                curr.val = val1
                break
                
            curr = curr.next
        
        n1 = 0
        curr = head
        while curr :
            
            n1+=1
            if n1==k :
                curr.val = val2
                break
            
            curr = curr.next
            
        return head
        
                
        
            
        
        
        