class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        dic = collections.Counter(nums)
        nums.sort()
        count = 0
        
        for i in range(len(nums)):
            
            if nums[i]>=k:
                break
                
            t = k - nums[i]
            if t>nums[i] and t in dic and dic[nums[i]]>0 :
                if dic[t]>0 :
                    dic[nums[i]] -= 1
                    dic[t] -= 1
                    count +=1
                    
            elif t == nums[i] :
                if dic[t]>=2 :
                    dic[t]-=2
                    count += 1
                
        
        return count         
            
            
        