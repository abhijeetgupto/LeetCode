class Solution:
    def minFlips(self, target: str) -> int:
        
        count = 0
        for char in target:
            
            if char == "0":
                if count%2 != 0:
                    count += 1 
            else:
                if count%2==0:
                    count += 1
        
        return count
                
        