class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        
        curr_sum = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)
        
        
        while True:
            
            largest = -heapq.heappop(target)
            if largest==1:
                break
                
            curr_sum -= largest
            if largest <= curr_sum or curr_sum<1:
                return False
            
            largest %= curr_sum
            curr_sum += largest
            heapq.heappush(target, -largest or -curr_sum)
            
            
        for num in target:
            if num != -1:
                return False
        return True
            
        