class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        curr = {}
        i = 0
        j = 1
        res = 0
        curr[fruits[i]] = 1
        
        while j<len(fruits) :
            
            if fruits[j] in curr :
                curr[fruits[j]] += 1
                j += 1
            
            elif len(curr) < 2 :
                curr[fruits[j]] = 1
                j += 1
            
            else:
                res = max(res, j-i)
                
                while len(curr)==2 and i<j :
                    
                    curr[fruits[i]] -= 1
                    if curr[fruits[i]] == 0:
                        curr.pop(fruits[i])
                    i += 1
                curr[fruits[j]] = 1
                j += 1
                
        res = max(res,j-i)
        return res
                
            
        