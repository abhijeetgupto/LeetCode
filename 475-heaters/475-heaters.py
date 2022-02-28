class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def checker(r):
            i = 0
            j = 0
            while j < len(houses) and i < len(heaters):
                num = houses[j]

                if num < heaters[i] - r:
                    return False

                elif num > heaters[i] + r:
                    i += 1

                else:
                    j += 1

            if j < len(houses) or i >= len(heaters):
                return False
            
            return True

            
        
        houses = list(sorted(set(houses)))
        heaters = list(sorted(set(heaters)))
        s = 0
        e = max(max(heaters),max(houses))
        res = e
        
        while s <= e :
            
            m = (s+e)//2
            if checker(m) :
                res = m
                e = m-1
                
            else:
                s = m+1
        
        return res
                
        