class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        def rec(l, i, j, memo = {}) :
            
            if (i,j) in memo :
                return memo[(i,j)]
            
            elif i>=len(l) :
                return 0
            
            else:
                memo[(i,j)] = max(rec(l,i+1,j), l[i]*j+rec(l,i+1,j+1))
                return memo[(i,j)]
        
        satisfaction.sort()
        x = rec(satisfaction, 0, 1)
        if x>0:
            return x
        return 0