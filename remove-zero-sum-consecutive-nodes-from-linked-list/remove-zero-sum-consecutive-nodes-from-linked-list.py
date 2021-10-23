# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []
        prefix = []
        curr = 0
        while head :
            res.append(head.val)
            curr += head.val
            prefix.append(curr)
            head = head.next
        
        dic = dict(collections.Counter(prefix))
        
        if 0 in dic :
            idx = len(prefix) - prefix[::-1].index(0) - 1
            prefix = prefix[idx+1 : ]
            res = res[idx+1 : ]
            
        # print(res)
        # print(prefix)
        
        temp = []
        i = 0
        while i < len(prefix) :
            curr = prefix[i]
            if dic[curr] > 1 :
                idx = len(prefix) - prefix[::-1].index(curr) - 1
                temp.append([i+1, idx+1])
                i = idx+1
            else:
                i += 1
        
        for l in temp :
            s,e = l
            for i in range(s,e):
                res[i] = None
        
        temp = []
        for val in res:
            if val :
                temp.append(val)
        if not temp:
            return 
        
        new = ListNode(temp.pop(0))
        curr = new
        while temp :
            curr.next = ListNode(temp.pop(0))
            curr = curr.next
        return new
        
                  
        
        
        