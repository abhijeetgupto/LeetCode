class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l=[]
        for node in lists:
            while node :
                bisect.insort(l,node.val)
                node = node.next
        if not l :
            return 
        new = ListNode(l.pop(0))
        curr = new
        
        while l :
            curr.next = ListNode(l.pop(0))
            curr = curr.next
            
        return new