class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        dic = {}
        for i in range(len(mat)) :
            dic[i] = mat[i].count(1)
        
        dic = dict(sorted(dic.items(), key = lambda x:x[1]))
        return list(dic.keys())[:k]
        