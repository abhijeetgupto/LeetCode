class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        s = set(nums)
        out = []
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                out.append(num)
        return out