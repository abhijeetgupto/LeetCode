class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        curr_sum = sum(nums)
        target = curr_sum/2
        count = 0
        heap = [-x for x in nums]
        heapq.heapify(heap)
        
        while curr_sum > target :
            
            x = -heapq.heappop(heap)/2
            curr_sum -= x
            heapq.heappush(heap, -x)
            count += 1
        
        return count
        
        
            
            
        