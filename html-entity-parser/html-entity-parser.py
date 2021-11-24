class Solution:
    def entityParser(self, text: str) -> str:
        
        dic = {'&quot;': '"', '&apos;': "'", '&amp;': '&', '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        
        res = ""
        curr = None
        
        for char in text :
            
            if curr is None :
                if char == '&' :
                    curr = '&'
                else:
                    res += char
            else:
                if char == ';' :
                    curr += char
                    if curr in dic :
                        res += dic[curr]
                    else:
                        res += curr
                    curr = None
                    
                elif char == '&' :
                    res += curr
                    curr = '&'
                
                else:
                    curr += char
        if curr is not None :
            res += curr
        return res
                    
                
        