import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(1, len(heights)):
            if heights[i] - heights[i-1] > 0 :
                heapq.heappush(heap, heights[i]-heights[i-1])
                if len(heap) > ladders :
                    bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i-1
            
        return i
        