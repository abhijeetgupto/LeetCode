class Solution:
    def numSplits(self, s: str) -> int:
        
        s1 = {s[0]:1}
        s2 = dict(collections.Counter(s[1:]))
        count = 0
        l1 = 1
        l2 = len(s2)
        
        if l1 == l2 :
            count += 1
        
        for i in range(1,len(s)):
            
            if s2[s[i]] == 1 :
                s2.pop(s[i])
                l2 -= 1
                
            else :
                s2[s[i]] -= 1
                
                
            if s[i] in s1 :
                s1[s[i]] += 1
            else:
                s1[s[i]] = 1
                l1 += 1
            
            if l1 == l2 :
                count+=1
        return count
        
        