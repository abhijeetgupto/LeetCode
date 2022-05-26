class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        res = []
        last = None
        
        for s in words:
            t = sorted(s)
            if last is None:
                res.append(s)
            else:
                if last!=t:
                    res.append(s)
            last = t
        
        return res