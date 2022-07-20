class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dic = {}
        for i,char in enumerate(s):
            if char not in dic:
                dic[char] = []
            dic[char].append(i)
        
        count = 0
        for word in words:
            flag = True
            idx = -1
            for char in word:
                if char not in dic:
                    flag = False
                    break
                else:
                    x = bisect_right(dic[char], idx)
                    if x==len(dic[char]):
                        flag = False
                        break
                    else:
                        idx = dic[char][x]
            if flag:
                count += 1
        
        return count