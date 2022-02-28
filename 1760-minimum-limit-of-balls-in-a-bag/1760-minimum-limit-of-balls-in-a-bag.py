class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def checker(k) :
            count = 0
            for num in nums :
                count += math.ceil(num/k)-1
                if count > maxOperations :
                    return False
            return True
        
        
        s = 1
        e = max(nums)
        res = e
        
        while s <= e :
            
            m = (s+e)//2
            
            if checker(m) :
                e = m-1
                res = m
            else:
                s = m+1
                
        return res