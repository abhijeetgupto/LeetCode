class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(node=0, parent=-1, color = 1):
            
            visited[node] = color
            for nbr in graph[node]:
                if visited[nbr] == 0:
                    if not dfs(nbr, node, 3-color):
                        return False
                
                elif nbr != parent and color == visited[nbr]:
                    return False
            
            return True
            
        visited = [0]*len(graph)
        for node in range(len(graph)):
            if visited[node] == 0 and not dfs(node, -1, 1):
                return False
            
        return True
