class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        n = len(cookies)
        res = [math.inf]
        
        def rec(i=0, curr=[0]*k, curr_max = 0):
            
            if i == n:
                res[0] = min(res[0], curr_max)
                return 
            
            if curr_max > res[0]:
                return 
            
            for child in range(k):
                curr[child] += cookies[i]
                rec(i+1, curr, max(curr_max, curr[child]))
                curr[child] -= cookies[i]
                
            return 
        
        rec()
        return res[0]
                
                
        