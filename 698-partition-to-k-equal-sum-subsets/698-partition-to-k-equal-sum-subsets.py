class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

        temp = [0]*k
        def rec(i=0):
            
            if i==n:
                return len(set(temp))==1
                
            for j in range(k):
                temp[j] += nums[i]
                if temp[j]<=target and rec(i+1):
                    return True
                temp[j] -= nums[i]
                if temp[j] == 0:
                    return False
                    
            return False
                    
                    
        n = len(nums)
        s = sum(nums)
        if s%k!=0:
            return False
        
        target = s//k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        return rec()
        
        
        
        
 