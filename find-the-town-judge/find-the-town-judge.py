class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        people = set(list(range(1,n+1)))
        dic = {}
        for l in trust :
            if l[0] in dic :
                dic[l[0]].add(l[1])
            else :
                dic[l[0]] = set([l[1]])
            if l[0] in people :
                people.remove(l[0])
                
        
        judge = list(people)
        
        if not judge or len(judge)>1 :
            return -1
        
        else:
            j = judge[0]
            for key in dic :
                if j not in dic[key] :
                    return -1
            return j
            
            
        