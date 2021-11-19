class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        dic = {}
        for word in words2 :
            temp = dict(collections.Counter(word))
            for key in temp :
                if key not in dic :
                    dic[key] = temp[key]
                else:
                    dic[key] = max(dic[key], temp[key])

        res = []
        for word in words1 :
            temp = collections.Counter(word)
            flag = False
            for key in dic :
                if key not in temp or dic[key] > temp[key] :
                    flag = True
                    break
            if not flag :
                res.append(word)
        return res
        