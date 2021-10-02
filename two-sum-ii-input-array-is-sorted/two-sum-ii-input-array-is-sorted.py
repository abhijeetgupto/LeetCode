class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(nums)-1
        while i<j:
            
            x = nums[i]+nums[j] 
            
            if x==target:
                return [i+1,j+1]
            elif x < target :
                i += 1
            else:
                j -= 1