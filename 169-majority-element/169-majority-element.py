class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = dict(collections.Counter(nums))
        m = max(dic.values())
        for key in dic:
            if dic[key] == m :
                return key
            
        