class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        def checker(sub) :
            
            n = len(sub)
            count = 0
            
            if n not in subs :
                return 0
                        
            for key in subs[n] :
                c = 0
                for i in range(n) :
                    if sub[i] != key[i] :
                        c += 1
                    if c>=2:
                        break
                if c==1 :
                        count += subs[n][key]
            return count
                    
        
        subs = {}
        for i in range(len(t)) :
            for j in range(i, len(t)):
                curr = t[i:j+1]
                n = len(curr)
                if n not in subs :
                    subs[n] = {}
                if curr not in subs[n] :
                    subs[n][curr] = 0
                subs[n][curr] += 1
        
            
        count = 0
        dic = {}
        
        for i in range(len(s)):
            for j in range(i, len(s)) :
                curr = s[i:j+1]
                if curr not in dic :
                    dic[curr] = checker(curr)
                count += dic[curr]
            
        return count
        