class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        
        k = 12
        cd = 1 #distance form center
        
        while k < neededApples :
            
            cd += 1
            k += 12*(cd**2)
        
        return cd*8
        