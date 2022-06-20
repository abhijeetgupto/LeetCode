class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        root = {}
        def addFolder(path):
            
            curr_node = root
            curr = "/"
            i = 1
            while i<len(path):
                if path[i]  == "/" :
                    if curr not in curr_node:
                        curr_node[curr] = {}
                    curr_node = curr_node[curr]
                    curr = "/"
                    i += 1
                else:
                    curr += path[i]
                    i+=1
            if curr not in curr_node:
                curr_node[curr] = {}
            curr_node = curr_node[curr]
            curr_node["*"] = "*"
        
        
        res = []
        def dfs(node,curr):
            
            if "*" in node:
                res.append(curr)
                return 
            
            for child in node:
                dfs(node[child], curr+child)
            
            return 
            
        
        for path in folder :
            addFolder(path)
        
        dfs(root,"")
        return res
        
        
        
            
            
        
        
        