class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort(reverse = True)
        res = 0
        x = 0
        for i in range(len(cost)) :
            if x==2:
                x=0
            else:
                res+=cost[i]
                x+=1
        return res
            
        
        