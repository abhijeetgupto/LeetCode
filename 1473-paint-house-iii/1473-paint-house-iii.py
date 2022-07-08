class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(None)
        def rec(i, count, last):
            
            if i==m:
                if count+1 == target:
                    return 0
                return math.inf
            
            if count >= target:
                return math.inf
                
            
            if houses[i] != 0:
                if houses[i] == last:
                    return rec(i+1, count, last)
                return rec(i+1, count+1, houses[i])
            
            else:
                res = math.inf
                for color in range(n):
                    if color+1 == last:
                        res = min(res, cost[i][color] + rec(i+1, count, last))
                    else:
                        res = min(res, cost[i][color] + rec(i+1, count+1, color+1))
                return res
                    

        if houses[0] == 0:
            res = math.inf
            for color in range(n):
                res = min(res, cost[0][color] + rec(1, 0, color+1))
            
        
        else:
            res = rec(1, 0, houses[0])
        
        if res!=math.inf:
            return res
        return -1
        