class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas)-sum(cost)<0:
            return -1
        
        n = len(gas)        
        curr = 0
        res = 0
        
        for i in range(n) :
            curr += gas[i]-cost[i]
            if curr<0:
                curr = 0
                res = i+1
        
        if res<n:
            return res
        return -1
        
        
                
                
                