class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        res = []
        
        def rec(i=0, k=target, curr=[]) :
            
            if  k == 0 :
                res.append(curr.copy())
                return 
            
            elif k<0 or i>=n :
                return 
            
            else:
                last = -1
                for j in range(i, n) :
                    if candidates[j] != last :
                        last = candidates[j]
                        curr.append(candidates[j])
                        rec(j+1, k-candidates[j], curr)
                        curr.pop()
                return 
        rec()
        return res
        