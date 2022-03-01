class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def checker(k) :
            count = 0
            for num in nums :
                count += math.ceil(num/k)
                if count>threshold :
                    return False
                
            return True

        
        s = 1
        e = 10**6
        res = e
        
        while s <= e :
            
            m = (s+e)//2
            if checker(m) :
                res = m
                e = m-1
                
            else:
                s = m+1
        
        return res
                
        
        