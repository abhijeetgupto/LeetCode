class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def checker(k):
            
            count = 0
            for c in quantities:
                count += math.ceil(c/k)
                if count>n:
                    break
            
            return count <= n
            
    
        left = 1
        right = max(quantities)
        res = right
        
        while left <= right:
            mid = (left+right)//2
            if checker(mid):
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res
                
            
        