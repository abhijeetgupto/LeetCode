import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap)>1 :
            x1 = -heapq.heappop(heap)
            x2 = -heapq.heappop(heap)
            if x1 != x2 :
                heapq.heappush(heap, -abs(x1-x2))
        
        if len(heap)==0:
            return 0
        return -heap[0]
                
        
        
        