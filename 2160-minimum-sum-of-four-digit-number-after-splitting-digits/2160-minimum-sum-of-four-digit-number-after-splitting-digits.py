class Solution:
    def minimumSum(self, num: int) -> int:
        
        nums = list(str(num))
        nums.sort()
        n1,n2,n3,n4 = nums
        
        return int(n1+n3) + int(n2+n4)
        