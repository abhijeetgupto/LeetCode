class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        dic = {}
        for i in range(len(labels)) :
            if labels[i] in dic :
                dic[labels[i]].append(values[i])
            else:
                dic[labels[i]] = [values[i]]
        
        for key in dic :
            dic[key].sort(reverse = True)
        dic = dict(sorted(dic.items(), key = lambda x:x[1], reverse = True))
        
        temp = []
        count = 0
        for key in dic:
            count+=1
            temp += dic[key][:useLimit]
            if count >= numWanted :
                break
        temp.sort(reverse = True)
        return sum(temp[:numWanted])