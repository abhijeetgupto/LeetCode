class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        nums[:] = [0]*c0 + [1]*c1 +[2]*c2