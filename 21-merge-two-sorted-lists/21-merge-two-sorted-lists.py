# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        curr = None
        
        while list1 and list2 :
            if list1.val > list2.val :
                temp = ListNode(list2.val)
                list2 = list2.next
                if curr :
                    curr.next = temp
                    curr = curr.next
                else:
                    curr = temp
                    head = temp
            
            else:
                temp = ListNode(list1.val)
                list1 = list1.next
                if curr :
                    curr.next = temp
                    curr = curr.next
                else:
                    curr = temp
                    head = temp
                    
        while list1 :
            temp = ListNode(list1.val)
            list1 = list1.next
            if curr :
                curr.next = temp
                curr = curr.next
            else:
                curr = temp
                head = temp
        
        while list2 :
            temp = ListNode(list2.val)
            list2 = list2.next
            if curr :
                curr.next = temp
                curr = curr.next
            else:
                curr = temp
                head = temp
                
        return head
            

    
    
                
                