class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s = set(nums)
        for i in range(len(nums)):
            x = target-nums[i]
            if x in s :
                for j in range(i+1,len(nums)):
                    if nums[j]==x:
                        return [i,j]
        