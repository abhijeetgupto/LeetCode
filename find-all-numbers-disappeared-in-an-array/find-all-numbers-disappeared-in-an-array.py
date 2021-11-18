class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        check = list(range(1,len(nums)+1))
        nums = set(nums)
        out=[]
        
        for num in check:
            if num not in nums:
                out.append(num)
        
        return out