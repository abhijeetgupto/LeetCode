class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def checker(k):
            
            curr = position[0]
            for _ in range(m-1):
                idx = bisect.bisect_left(position, curr+k)
                if idx==n:
                    return False
                curr = position[idx]
            return True
                
        
        
        
        position.sort()
        n = len(position)
        s = 1
        e = max(position) - min(position)
        res = 1
        
        while s<=e:
            mid = (s+e)//2
            
            if checker(mid):
                s = mid+1
                res = mid
            
            else:
                e = mid-1
        return res
        