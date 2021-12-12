class Solution:
    def countPoints(self, rings: str) -> int:
        
        dic = {}
        for i in range(1,len(rings),2) :
            if rings[i] in dic :
                dic[rings[i]].add(rings[i-1])
            
            else:
                dic[rings[i]] = {rings[i-1]}
        
        count = 0
        for key in dic :
            if len(dic[key]) == 3 :
                count += 1
        
        return count
                
        