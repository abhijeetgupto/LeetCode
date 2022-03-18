class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        dic = dict(collections.Counter(s))
        res = ""
        for i in range(len(s)) :
            
            if s[i] not in res :
                if dic[s[i]] == 1 :
                    res += s[i]
                    dic.pop(s[i])
                         
                else:
                    flag = False
                    temp = {}
                    
                    for j in range(i+1, len(s)) :
                        
                        if s[j] not in res : 
                            
                            if s[j] not in temp :
                                temp[s[j]] = 1
                            else:
                                temp[s[j]] += 1
                                
                            if s[j] < s[i] :
                                flag = True
                                break
                                
                            if dic[s[j]] == 1:
                                flag = False
                                break
                            
                            if temp[s[j]] == dic[s[j]] :
                                flag = False
                                break
                                
                    if not flag :
                        res += s[i]
                        dic.pop(s[i])
                    else:
                        dic[s[i]] -= 1
                    
        return res
                    
                    
                    
                    
            
            
                
                
                
        