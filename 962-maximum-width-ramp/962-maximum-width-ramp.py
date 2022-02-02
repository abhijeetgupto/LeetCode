from collections import defaultdict

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        dic = defaultdict(list)
        for i in range(n):
            dic[nums[i]].append(i)

        dic = dict(sorted(dic.items(), key=lambda x: x[0]))
        
        visited = set()
        m = n-1
        res = 0
        
        for key in dic :
            res = max(res, dic[key][-1]-dic[key][0])
            for num in dic[key] :
                visited.add(num)
            while m in visited :
                m -= 1
            
            res = max(res, m-dic[key][0])
            
        return res
            
        
        
        