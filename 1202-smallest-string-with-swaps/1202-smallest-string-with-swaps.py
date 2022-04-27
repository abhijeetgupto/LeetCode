class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        parent = list(range(len(s)))
        
        def find(x):
            if parent[x] == x :
                return x
            parent[x] = find(parent[x])
            return parent[x]

                           
        for i,j in pairs :
            x1 = find(i)
            x2 = find(j)
            if x1!=x2 :
                parent[x1] = x2
        
        for i in range(len(parent)) :
            if parent[i] != i :
                parent[i] = find(parent[i])
        
        dic = {}
        for i in range(len(parent)) :
            if parent[i] not in dic :
                dic[parent[i]] = []
            dic[parent[i]].append(i)
        
        res = [""]*len(s)
        
        for key in dic :
            chars = []
            idxs = []
            for i in dic[key] :
                chars.append(s[i])
                idxs.append(i)
                
            idxs.sort()
            chars.sort()
            
            for i in range(len(idxs)) :
                res[idxs[i]] = chars[i]
        
        return "".join(res)
                
                
        
        
        