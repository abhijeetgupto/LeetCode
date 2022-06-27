class Solution:
    def minPartitions(self, n: str) -> int:
        
        res = 0
        for char in n:
            res = max(int(char),res)
        return res
        