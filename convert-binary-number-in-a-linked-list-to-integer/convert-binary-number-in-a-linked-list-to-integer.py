# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l=[]
        while head != None:
            l.append(head.val)
            head=head.next
        sum=0
        l.reverse()
        for i in range(len(l)):
            sum+=l[i]*(2**i)
        
        return sum
            
        