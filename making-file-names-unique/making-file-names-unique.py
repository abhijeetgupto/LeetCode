class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        dic = {}
        res = []
        
        for name in names :
            if name in dic :
                temp = name + f"({dic[name]+1})"
                dic[name] += 1
                while temp in dic:
                    temp = name + f"({dic[name]+1})"
                    dic[name] += 1
                dic[temp] = 0
                res.append(temp)
            else :
                dic[name] = 0
                res.append(name)
        return res
                
                
        