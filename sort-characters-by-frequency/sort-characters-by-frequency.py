class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = dict(collections.Counter(s))
        
        dic = dict(sorted(dic.items(), key=lambda x: (x[1],x[0]), reverse=True))
        result = ""
        
        for key in dic:
            result += key*dic[key]
        
        return result