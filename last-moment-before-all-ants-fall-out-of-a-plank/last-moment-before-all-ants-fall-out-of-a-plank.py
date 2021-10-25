class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        for i in range(len(right)):
            right[i] =  n - right[i]
        
        temp = left+right
        if not temp:
            return 0
        return max(temp)