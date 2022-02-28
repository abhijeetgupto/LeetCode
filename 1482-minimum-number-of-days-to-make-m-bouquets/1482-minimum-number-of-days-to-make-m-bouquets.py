class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def checker(x):
            count = 0
            curr = 0
            for num in bloomDay :
                
                if x >= num :
                    curr += 1
                else:
                    curr = 0
                    
                if curr == k :
                    count += 1
                    curr = 0
                    
            return count >= m
            
        s = 1
        e = max(bloomDay)
        res = -1
        
        while s <= e :
            
            mid = (s+e)//2
            
            if checker(mid) :
                res = mid
                e = mid-1
            
            else:
                s = mid+1
                 
        return res
        