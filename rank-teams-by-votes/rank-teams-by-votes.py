class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        if len(votes)==1:
            return votes[0]
        
        dic = {}
        
        x = votes[0]
        for char in x :
            dic[char] = [0]*len(x)
        
        for vote in votes :
            for i in range(len(vote)) :
                dic[vote[i]][i] -= 1
            
        dic = dict(sorted(dic.items(),key=lambda x: (x[1],x[0])))
        return "".join(dic.keys())