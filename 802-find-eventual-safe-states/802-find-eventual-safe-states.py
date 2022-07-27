class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        def dfs(node):
            
            visited[node] = True
            curr[node] = True
            
            for nbr in graph[node]:
                if not visited[nbr]:
                    if dfs(nbr):
                        return True
                elif curr[nbr]:
                    return True
                
            res.append(node)
            curr[node] = False
            return False
        
        n = len(graph)
        visited = [False]*n
        curr = [False]*n
        res = []
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        res.sort()
        return res
            
                
        