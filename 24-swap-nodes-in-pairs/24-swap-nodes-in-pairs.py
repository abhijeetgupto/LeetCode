class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l = []
        while head :
            l.append(head.val)
            head = head.next
            
        if not l :
            return
        
        res = []
        for i in range(0,len(l),2):
            temp = l[i:i+2]
            temp.reverse()
            res[i:i+2] = temp
        
        new = ListNode(res.pop(0))
        curr = new
        while res :
            curr.next = ListNode(res.pop(0))
            curr = curr.next
        return new