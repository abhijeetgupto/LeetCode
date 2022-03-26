class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix = [arr[0]]
        
        for i in range(1, len(arr)) :
            prefix.append(arr[i]^prefix[-1])
        
        res = []
        
        for l,r in queries :
            if l == 0 :
                res.append(prefix[r])
            else:
                res.append(prefix[r]^prefix[l-1])
                
        return res
            