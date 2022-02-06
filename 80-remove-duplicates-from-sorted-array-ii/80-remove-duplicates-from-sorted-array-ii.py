import collections
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = dict(collections.Counter(nums))
        count = 0
        res = []
        for key in dic :
            if dic[key]==1:
                res.append(key)
            if dic[key] >=2 :
                res.append(key)
                res.append(key)
                
        nums[:]  = res
        return len(res)