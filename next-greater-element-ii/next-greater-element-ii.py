class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        nums = nums*2
        res = [-1]*len(nums)
        stack = []
        for i in range(len(nums)) :
            temp = nums[i]
            while stack and temp > nums[stack[-1]] :
                idx = stack.pop()
                res[idx] = temp
            stack.append(i)
        return res[:len(nums)//2]
        
        