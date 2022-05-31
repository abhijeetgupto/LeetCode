import bisect
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        if n==3:
            return sum(nums)
        
        nums.sort()
        k = math.inf
        ans = 0
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                curr = nums[i]+nums[j]
                diff = target-curr
                idx = bisect.bisect_left(nums, diff)
                n1=n2=n3 = math.inf
                v = [-1,0,1]
                for val in v:
                    if idx+val in range(n) and idx+val!=i and idx+val!=j:
                        num3 = nums[idx+val]
                        if abs(target-(curr+num3)) < k:
                            k = abs(target-(curr+num3))
                            ans = curr+num3
                    
                
        return ans

            
                        
                        
                