class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        
        dp = [[None for _ in range(2002)] for _ in range(len(pairs)+1)]
        def rec(i=0, curr_right=0) :
            
            if dp[i][curr_right] is not None:
                return dp[i][curr_right]
            
            if i >= len(pairs) :
                return 0
            
            if curr_right is None :
                dp[i][curr_right] = max(rec(i+1, pairs[i][1]), rec(i+1, curr_right))
            
            else:
                if pairs[i][0] > curr_right  :
                    dp[i][curr_right] = max(1+rec(i+1, pairs[i][1]), rec(i+1, curr_right))
                
                else:
                    dp[i][curr_right] = rec(i+1, curr_right)
            
            return dp[i][curr_right]
        
        for i in range(len(pairs)) :
            pairs[i][0] += 1001
            pairs[i][1] += 1001
            
        return rec()
    
        
        
        
            
            
            
        