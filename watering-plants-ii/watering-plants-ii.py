class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        currA = capacityA
        currB = capacityB
        count = 0 
        
        while plants :
            
            if len(plants) >= 2 :
                
                currA -= plants.pop(0)
                currB -= plants.pop()
                
                if len(plants) >= 2 :
                    if plants[0] > currA :
                        currA = capacityA
                        count += 1
                    if plants[-1] > currB :
                        currB = capacityB
                        count += 1
                
                elif len(plants) == 1 :
                    
                    if plants[0] > currA and plants[0] > currB :
                        count += 1
                        break
                    else:
                        break
                        
            elif len(plants) == 1 :
                
                if plants[0] > currA and plants[0] > currB :
                    count += 1
                    break
                else:
                    break
        return count
                
                
            
                
                
            
            
        
        