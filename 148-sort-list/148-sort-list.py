class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = []
        while head :
            l.append(head.val)
            head = head.next
        l.sort()
        if not l :
            return 
        new = ListNode(l.pop(0))
        curr = new
        while l :
            curr.next = ListNode(l.pop(0))
            curr = curr.next
        return new
        