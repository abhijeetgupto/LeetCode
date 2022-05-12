class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        s = set()
        n = len(nums)
        
        def rec(curr=[], visited = set()):
            
            if len(curr) == n:
                temp = tuple(curr)
                s.add(temp)
            
            for i in range(len(nums)) :
                if i not in visited:
                    rec(curr + [nums[i]], visited.union(set([i])))
        rec()
        return s
                
        