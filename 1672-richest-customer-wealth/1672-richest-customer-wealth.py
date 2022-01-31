class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        res = 0
        for l in accounts :
            res = max(res, sum(l))
        return res
        