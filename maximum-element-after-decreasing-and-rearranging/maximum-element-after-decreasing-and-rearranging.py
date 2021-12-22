class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        dic = dict(collections.Counter(arr))
        heap = list(dic.keys())
        heap.sort()
        res = 1
                
        x = heap.pop(0)
        if not heap:
            return min(x,dic[x])
        
        if x == 1 or dic[x] == 1 :
            last = 1
        else:
            m2 = dic[x]-1
            last = min(x, m2+1, heap[0])
        
        while heap :
            x = heap.pop(0)
            last = min(last+dic[x], x)
        
        return last
        
            
            
            
            
        