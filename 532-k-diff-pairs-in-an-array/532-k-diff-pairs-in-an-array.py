class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        dic = dict(collections.Counter(nums))
        count = 0
        if k == 0 :
            for key in dic :
                if dic[key]>=2 :
                    count += 1
            return count
        
        for key in dic :
            if k+key in dic :
                count += 1
        return count
        