class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        n = len(piles)
        memo = {}
        
        def rec(i=0, t=k) :
            
            if (i,t) in memo :
                return memo[(i,t)]
            
            if i>=n or t == 0 :
                return 0
            
            
            res = rec(i+1, t)
            temp = 0
            
            for j in range(min(len(piles[i]), t)) :
                temp += piles[i][j]
                res = max(res, temp+rec(i+1,t-j-1))
            
            memo[(i,t)] = res
            return res
        
        return rec()
                
            
            
            
            
            
            
                    
                
                
        