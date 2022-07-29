class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def helper(word):
            dic = {}
            res = ""
            i = 0
            for char in word :
                if char not in dic :
                    dic[char] = i
                    res += str(i) + "/"
                    i += 1
                else :
                    res += str(dic[char]) + "/"
            return res
        
        target = helper(pattern)
        res = []
        for word in words :
            temp = helper(word)
            if temp==target :
                res.append(word)
        return res