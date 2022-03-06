class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        nums = sorted(set(nums))
        last = 1
        count = 0
        
        for i in range(len(nums)) :
            
            n = nums[i] - last
            if n>=1 : 
                if n>k :
                    s = last
                    count += (k)*(2*s + (k-1))//2
                    k = 0
                    break
                
                else:
                    s = last
                    count += (n)*(2*s + (n-1))//2
                    k -= n
                    
            last = nums[i]+1
        
          
        if k>0 :
            count += (k)*(2*last + (k-1))//2
            
        return count
            
            
            
            
        