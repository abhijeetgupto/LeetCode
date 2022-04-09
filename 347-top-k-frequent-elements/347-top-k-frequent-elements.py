class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = collections.Counter(nums)
        dic = dict(sorted(dic.items(), key=lambda x:-x[1]))
        return list(dic.keys())[:k]
        