class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def dfs(node):
            
            if node not in dic:
                visited[node] = True
                return 
            
            visited[node] = True
            for nbr in dic[node]:
                if not visited[nbr]:
                    dfs(nbr)
            
        if len(connections) < n-1:
            return -1
        
        visited = [False]*n
        dic = {}
        for i,j in connections:
            if i not in dic:
                dic[i] = set()
            if j not in dic:
                dic[j] = set()
                
            dic[i].add(j)
            dic[j].add(i)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count-1
        
        
        
                
        
        