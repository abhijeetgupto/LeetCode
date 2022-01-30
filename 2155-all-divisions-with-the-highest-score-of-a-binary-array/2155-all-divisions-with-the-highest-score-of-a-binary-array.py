class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        total_one = nums.count(1)
        zero = 0
        one = 0
        temp = [0]*(len(nums)+1)
        temp[0] = total_one
        
        for i in range(len(nums)) :
            if nums[i]==0:
                zero+=1
            else:
                one+=1
                
            temp[i+1] = zero+total_one-one
        m = max(temp)   
        res = []
        for i in range(len(temp)) :
            if temp[i] == m:
                res.append(i)
        return res
            
        
        
        
        
        