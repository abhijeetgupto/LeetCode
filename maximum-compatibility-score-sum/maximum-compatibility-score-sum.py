class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        scores = []
        for s in students :
            l = []
            for m in mentors :
                score = 0
                for i in range(len(m)) :
                    if m[i]==s[i] :
                        score += 1
                l.append(score)
            scores.append(l)

        temp = list(range(len(scores)))
        p = list(itertools.permutations(temp))
 
        res = 0
        for l in p :
            j = 0
            t = 0 
            for i in l :
                t += scores[j][i] 
                j += 1
            res = max(res,t)
            
        return res
                
        
        
        
        
        
        
            
            
        
        
