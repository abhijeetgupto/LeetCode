class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes, key = lambda x:-x[1])
        i = 0
        res = 0
        
        while truckSize>0 and i<len(boxTypes):
            
            if boxTypes[i][0] <= truckSize:
                truckSize -= boxTypes[i][0]
                res += boxTypes[i][0]*boxTypes[i][1]
            
            else:
                res += truckSize*boxTypes[i][1]
                truckSize = 0
            
            i+=1
            
        return res
        