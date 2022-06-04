class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        curr_slow = head
        curr_fast = head
        
        while curr_fast:
            
            curr_fast = curr_fast.next
            if curr_fast is None:
                return curr_slow
            
            curr_fast = curr_fast.next
            curr_slow = curr_slow.next
        
        return curr_slow
        