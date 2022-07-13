class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        
        buses.sort()
        passengers.sort()
      
        
        last = 0
        res = 0
        
        for num in buses:
            idx = bisect.bisect_right(passengers, num)
            j = min(idx, last+capacity)
            
            if j == last:
                res = num
                
            elif j-last < capacity:
                k = num
                flag = False
                for x in range(j-1, last-1, -1):
                    if passengers[x] != k:
                        res = k
                        flag = True
                        break
                    k -= 1
                        
                if not flag:
                    if last != 0 and passengers[last-1] != passengers[last]-1:
                        res = passengers[last]-1
                    elif last == 0:
                        res = passengers[last]-1

            else:
                k = passengers[j-1]
                flag = False
                for x in range(j-1, last-1, -1):
                    if passengers[x] != k:
                        res = k
                        flag = True
                        break
                    k -= 1
                
                if not flag and passengers[last] <= num:
                    if last != 0 and passengers[last-1] != passengers[last]-1:
                        res = passengers[last]-1
                    elif last == 0:
                        res = passengers[last]-1
                    
                    

            last = j
            
           
        return res
 