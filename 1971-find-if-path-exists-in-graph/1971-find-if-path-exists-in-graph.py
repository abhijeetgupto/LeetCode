class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, target: int) -> bool:
        
        if source == target :
            return True
        
        dic = {}
        
        for n1,n2 in edges :
            
            if n1 not in dic :
                dic[n1] = []
            if n2 not in dic :
                dic[n2] = []
            
            dic[n1].append(n2)
            dic[n2].append(n1)
        
        if source not in dic :
            return False
        
        stack = dic[source]
        visited = {source}
        
        while stack :
            top = stack.pop()
            if top == target :
                return True
            
            if top in dic :
                for key in dic[top] :
                    if key not in visited :
                        stack.append(key)
            visited.add(top)
            
        return False
                    
            
        