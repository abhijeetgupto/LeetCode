class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        arr = []
        for i in range(len(aliceValues)):
            arr.append([-(aliceValues[i] + bobValues[i]),i])
        
        heapq.heapify(arr)
        a = 0
        b = 0
        flag = True
        
        while arr :
            
            if flag :
                flag = False
                x = heapq.heappop(arr)
                a += aliceValues[x[1]]
                
            
            else:
                flag = True
                x = heapq.heappop(arr)
                b += bobValues[x[1]]
        if a==b:
            return 0
        if a>b:
            return 1
        
        return -1
                
            
        
        
        
        
        