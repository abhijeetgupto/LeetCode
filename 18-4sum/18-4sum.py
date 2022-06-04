class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        dic = collections.Counter(nums)
        nums.sort()
        res = set()
        for i in range(len(nums)):
            dic[nums[i]] -= 1
            for j in range(i+1,len(nums)):
                dic[nums[j]] -= 1
                for k in range(j+1,len(nums)):
                    dic[nums[k]] -= 1
                    x  = target-(nums[i]+nums[j]+nums[k])
                    if x in dic and dic[x]>0:
                        temp = tuple(sorted([nums[i],nums[j],nums[k],x]))
                        res.add(temp)
                    dic[nums[k]] += 1
                dic[nums[j]] += 1
            dic[nums[i]] += 1
        
        return res               