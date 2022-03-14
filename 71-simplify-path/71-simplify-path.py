class Solution:
    def simplifyPath(self, path: str) -> str:
        
        n = len(path)
        l = []
        i=0
        curr = ""
        
        while i<n :
            
            if path[i] == "." :

                temp = curr
                curr = ""
                while i<n and path[i] != "/" :
                    temp += path[i]
                    i+=1
                if temp == ".." :
                    if l:
                        l.pop()
                elif len(temp) >= 2 :
                    l.append(temp)
                
                  
                
            elif path[i] == "/" :
                if curr : l.append(curr)
                curr = ""
                while i<n and path[i] == "/" :
                    i+=1
            
            else:
                curr += path[i]
                i+=1
        
        if curr:
            l.append(curr)
        
        res = "/" + "/".join(l)
        return res
        
            
                
                
                
        
                    
            
            