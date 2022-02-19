class Solution:
    def knightDialer(self, n: int) -> int:
        
        dic = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        memo = {}
        
        def rec(curr, k) :
            
            if (curr,k) in memo:
                return memo[(curr,k)]
            
            if k==0 :
                return 1
            
            else:
                count = 0
                for num in dic[curr] :
                    count += rec(num, k-1)
                
                memo[(curr,k)] = count
                return count
            
        res = 0
        for i in range(10):
            res += rec(i,n-1)
        
        return res%((10**9) +7)
                    
        