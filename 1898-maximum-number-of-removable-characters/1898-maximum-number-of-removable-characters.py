class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        
        def checker(k):
            
            temp = set(removable[:k])
            s_idx = 0
            p_idx = 0
            while p_idx < len(p) and s_idx < len(s):
                
                if s_idx not in temp:
                    if s[s_idx] == p[p_idx]:
                        s_idx+=1
                        p_idx+=1
                    else:
                        s_idx+=1
                
                else:
                    s_idx += 1
                    
            return p_idx == len(p)

            
        left = 0
        right = len(removable)
        res = left
        
        while left<=right:
            mid = (left+right)//2
            if checker(mid):
                res = mid
                left = mid+1
            else:
                right = mid-1
        
        return res