class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        n = len(cookies)
        res = [math.inf]
        
        def rec(i=0, curr=[0]*k):
            
            if i == n:
                res[0] = min(res[0], max(curr))
                return 
            
            if max(curr) > res[0]:
                return 
            
            for child in range(k):
                curr[child] += cookies[i]
                rec(i+1, curr)
                curr[child] -= cookies[i]
                
            return 
        
        rec()
        return res[0]
                
                
        