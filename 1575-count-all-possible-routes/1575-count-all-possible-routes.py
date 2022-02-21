class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        memo = {}
        def rec(curr = start, p=fuel) :
            
            if (curr, p) in memo:
                return memo[(curr,p)]
            
            if p<0 :
                return 0
            
            if curr == finish :
                count = 1
                for i in range(len(locations)) :
                    if curr != i :
                        count += rec(i, p-abs(locations[curr] - locations[i]))
                        
                memo[(curr,p)] = count
                return count
                
            elif p>0 :
                count = 0
                for i in range(len(locations)) :
                    if curr != i :
                        count += rec(i, p-abs(locations[curr] - locations[i]))
                        
                memo[(curr,p)] = count
                return count
            
            else:
                return 0
        
        mod = 10**9 + 7
        return rec()%mod
            
            
                    
            
        