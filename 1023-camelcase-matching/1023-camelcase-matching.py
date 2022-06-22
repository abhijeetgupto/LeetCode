class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        n = len(pattern)
        
        root = {}
        def addword(i, word):
            curr_node = root
            for char in word:
                
                if char not in curr_node:
                    curr_node[char] = {}
                curr_node = curr_node[char]
            
            curr_node["*"] = i
            return 
        
        
        res = [False]*len(queries)
        
        def dfs(node=root, i=0):
            
            if i==n:
                for key in node:
                    if key == "*":
                        res[node[key]] = True
                    elif key.islower():
                        dfs(node[key], i)
                return 
                
            for key in node:
                if key == pattern[i]:
                    dfs(node[key], i+1)
                    
                elif key.islower():
                    dfs(node[key], i)
            return 
        

        
        for i,word in enumerate(queries):
            addword(i,word)
        
        dfs()
        return res
        
        