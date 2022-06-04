from collections  import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        dic = defaultdict(int)
        n = len(nums1)
        
        for i in range(n):
            for j in range(n):
                dic[nums1[i]+nums2[j]]+=1
        
        res = 0
        for i in range(n):
            for j in range(n):
                res += dic[-(nums3[i]+nums4[j])]
        
        return res
        