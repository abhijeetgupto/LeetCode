class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        res = [0]*len(rains)
        full = {}
        idx = []
        last = 1
        
        for i in range(len(rains)):
            
            if rains[i] == 0 :
                idx.append(i)
                res[i] = last
                
            else:
                if rains[i] in full :
                    if not idx or idx[-1] < full[rains[i]] :
                        return []
                    else: 
                        j = bisect.bisect_right(idx, full[rains[i]])
                        res[idx[j]] = rains[i]
                        idx.pop(j)
                        res[i] = -1
                        full[rains[i]] = i
                    
                else:
                    full[rains[i]] = i
                    res[i] = -1
                last = rains[i]
                    
        return res