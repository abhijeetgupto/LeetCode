class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def bfs(node):
            
            visited[node] = True
            queue = deque([node])
            
            while queue:
                
                node = queue.popleft()
                if node in dic:
                    for v in dic[node]:
                        if not visited[v] :
                            visited[v] = True
                            queue.append(v)

            
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
                bfs(i)

        return count-1