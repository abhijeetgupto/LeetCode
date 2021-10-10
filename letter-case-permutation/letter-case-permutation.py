class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        def helper(characters) :
            if len(characters) == 1 :
                return [[characters[0]],[characters[0].upper()]]
                
            else:
                l = []
                for i in range(len(characters)):
                    for j in helper(characters[i+1 :]) :
                        l.append([characters[i]] + j )
                        l.append([characters[i].upper()] + j)
                return l

        s = s.lower()
        chars = []
        for char in s :
            if ord(char) in range(97, 123):
                chars.append(char)
                
        if not chars:
            return [s]
        
        
        temp = helper(chars)

        
        res = []
        for combination in temp :
            combi = ""
            if len(combination)<len(chars):
                break
            for char in s :
                if ord(char) in range(48,58) :
                    combi += char
                else:
                    combi += combination.pop(0)
            res.append(combi)
        return res
            