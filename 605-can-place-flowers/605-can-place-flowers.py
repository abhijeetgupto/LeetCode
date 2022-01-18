class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n==0:
            return True
        
        if len(flowerbed) == 1 :
            if n==1 and flowerbed == [0]:
                return True
            return False
               
        i = 0
        while i < len(flowerbed) and n>0 :
            
            if flowerbed[i] == 0 :
                if i==0 :
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i==len(flowerbed)-1 :
                    if flowerbed[i-1] == 0 :
                        flowerbed[i]=1
                        n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 :
                        flowerbed[i] = 1
                        n -= 1
            i+=1
        return n==0
                    
                        
                
                