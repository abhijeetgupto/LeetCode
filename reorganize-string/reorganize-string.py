import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        dic = dict(collections.Counter(s))        
        heap = []
        heapq.heapify(heap)
        for key in dic:
            heapq.heappush(heap, [-dic[key], key])
        res = ""
        while heap:
            x = heapq.heappop(heap)

            if not res or res[-1] != x[1]:
                res += x[1]
                if x[0] != -1:
                    x[0] += 1
                    heapq.heappush(heap, x)
            else:
                if not heap :
                    return ""
                x_new = heapq.heappop(heap)
                heapq.heappush(heap, x)
                res += x_new[1]
                if x_new[0] != -1:
                    x_new[0] += 1
                    heapq.heappush(heap, x_new)
        return res
                
                    
        
        
        
        
        
            
            
            
            
            
            
        