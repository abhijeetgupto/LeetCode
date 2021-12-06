class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        dic = {}
        for num in set(position):
            dic[num] = position.count(num)
        counte=0
        counto=0
        for key in dic :
            if key%2==0:
                counte += dic[key]
            else:
                counto += dic[key]
        
        return min(counte,counto)
                    
        
        
                
            
        
        
        
        
        