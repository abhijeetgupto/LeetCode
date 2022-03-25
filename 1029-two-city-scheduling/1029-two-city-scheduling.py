class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        n2 = n//2
        
        memo = {}
        def rec(i=0, a=0, b=0) :
            
            
            if (i,a) in memo:
                return memo[(i,a)]
            
            if i >= n :
                return 0
            
            else:
                if a < n2 and b < n2 :
                    memo[(i,a)] =  min(costs[i][0]+rec(i+1,a+1,b), costs[i][1]+rec(i+1,a,b+1))
                
                elif a<n2 :
                    memo[(i,a)] = costs[i][0]+rec(i+1,a+1,b)
                
                elif b<n2 :
                    memo[(i,a)] =  costs[i][1]+rec(i+1,a,b+1)
                
                return memo[(i,a)]
        
        return rec()
        