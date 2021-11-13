class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], l1: int, l2: int) -> int:
        
        
        if len(nums) == l1+l2:
            return sum(nums)
        
        prefix = [0]
        curr = 0
        for num in nums :
            curr += num
            prefix.append(curr)
        
     
        res = 0
        
        for i in range(len(prefix)-l1):
            
            s1 = prefix[i+l1] - prefix[i]
            s2 = 0
            
            for j in range(0,i) :
                if  j+l2 < i :
                    s2 = max(s2, prefix[j+l2] - prefix[j])
                else:
                    break
            
            for j in range(i+l1, len(prefix)) :
                if j+l2 < len(prefix) :
                    s2 = max(s2, prefix[j+l2] - prefix[j])
                else:
                    break
                    
            res = max(res, s1+s2)
            
        return res
            
        