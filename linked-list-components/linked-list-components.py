# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        nums = set(nums)
        curr = False
        count = 0
        
        while arr :
            top = arr.pop(0)
            if top in nums :
                if not curr :
                    count += 1
                    curr = True       
            else :
                curr = False
                
        return count
                
        
        
        