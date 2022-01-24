class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def kadaneAlgo(nums):
            if len(nums) == 0:
                return float("-inf");
            best = max(nums);
            prev = 0; # if set as float('-inf') then there is posibility to have number overflow
            
            for i in nums:
                prev = i + max(0,prev);
                best = max(prev,best);
            
            return best;
        
        res1 = kadaneAlgo(nums);
        
        negNums = [-nums[x] for x in range(1,len(nums)-1)];
        minSubArrary = -kadaneAlgo(negNums);
        numsSum = sum(nums);
        res2 = numsSum - minSubArrary;
        
        return max(res1,res2);