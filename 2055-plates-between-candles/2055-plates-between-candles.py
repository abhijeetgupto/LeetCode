class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        candels, res, prefix = [],[],[0]
        
        for i in range(len(s)):
            if s[i] != '*' :
                candels.append(i)
        
        
        for i in range(1, len(candels)):
            prefix.append(prefix[-1]+candels[i]-candels[i-1]-1)
        
        for left,right in queries:
            
            idx1 = bisect.bisect_left(candels, left)
            idx2 = bisect.bisect_right(candels, right)
            if idx1 == idx2:
                x = 0
            elif idx2 == len(candels) or candels[idx2] > right:
                x = prefix[idx2-1] - prefix[idx1]
            else:
                x = prefix[idx2]-prefix[idx1]
            
            res.append(x)
        
        return res
        
                