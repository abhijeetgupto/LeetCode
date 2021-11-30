class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if k == len(s):
            return True
        if k>len(s) :
            return False
    
        dic = dict(collections.Counter(s))
        odd = 0
        even = 0
        for key in dic:
            if dic[key]%2 == 0:
                even+=1
            else:
                odd+=1
        
        if odd > k:
            return False
        
        return True
        
        