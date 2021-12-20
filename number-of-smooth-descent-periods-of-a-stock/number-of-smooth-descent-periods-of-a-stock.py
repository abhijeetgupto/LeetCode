class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        count = n
        last = prices[0]
        curr = 1
        
        for i in range(1,n) :
            
            if prices[i] == last-1 :
                last = prices[i]
                curr += 1
            
            else:
                count += ((curr)*(curr-1))//2
                curr = 1
                last = prices[i]
            
        count += ((curr)*(curr-1))//2   
        return count