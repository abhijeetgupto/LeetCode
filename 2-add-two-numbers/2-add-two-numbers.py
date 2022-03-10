# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
                
        x = l1.val + l2.val
        carry = 0
        
        if x > 9 :
            carry = int(str(x)[0])
            x =  int(str(x)[1])
            
        l1 = l1.next
        l2 = l2.next
        new = ListNode(x)
        curr = new
        
        while l1 or l2 :
            
            if l1 and l2 :
                x = carry + l1.val + l2.val
                if x > 9 :
                    carry = int(str(x)[0])
                    x =  int(str(x)[1])
                    
                else:
                    carry = 0
                    
                curr.next = ListNode(x)
                curr = curr.next
                l1 = l1.next
                l2 = l2.next
                
            elif l1 :
                x = carry + l1.val
                if x > 9 :
                    carry = int(str(x)[0])
                    x =  int(str(x)[1])
                else:
                    carry = 0
                curr.next = ListNode(x)
                curr = curr.next
                l1 = l1.next
                
            elif l2 :
                x = carry + l2.val
                if x > 9 :
                    carry = int(str(x)[0])
                    x =  int(str(x)[1])
                else:
                    carry = 0
                curr.next = ListNode(x)
                curr = curr.next
                l2 = l2.next
        
        
        if carry>0:
            curr.next = ListNode(carry)
        
        return new
                
                
                
                
                
                
                
        