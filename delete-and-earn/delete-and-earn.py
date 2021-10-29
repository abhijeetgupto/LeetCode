class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        def helper(nums) :
            
            if len(nums) <=  2 :
                return max(nums)
        
            if len(nums) == 3 :
                return max(nums[1],nums[0]+nums[2])

            dp = [0]*len(nums)
            dp[0],dp[1],dp[2] = nums[0],nums[1],max(nums[2]+nums[0],nums[1])


            for i in range(3, len(dp)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2], nums[i]+dp[i-3])

            return dp[-1]

        dic = collections.Counter(nums)
        keys = list(dic.keys())
        keys.sort()
        
        res = []
        last = keys.pop(0)
        temp = [last*dic[last]]
        while keys :
            top = keys.pop(0)
            if top == last+1 :
                temp.append(top*dic[top])
                last = top
            else:
                res.append(temp)
                temp = [top*dic[top]]
                last = top
        res.append(temp)
    
        count = 0
        for l in res:
            count += helper(l)
        return count
             
        
                        
                    
                
                
                
        
        
            
            
            
        
        
        