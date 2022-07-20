class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        
        
        def cycle(node):
           
            visited[node] = True
            curr[node] = True
            
            if node in dic:
                for nbr in dic[node]:
                    if not visited[nbr]:
                        if cycle(nbr):
                            curr[node] = False
                            return True
                    elif curr[nbr]:
                        curr[node] = False
                        return True
                    
            curr[node] = False
            return False
            

        def dfs(node):
            
            visited[node] = True
            if node in dic:
                for nbr in dic[node]:
                    if not visited[nbr]:
                        dfs(nbr)
            res.appendleft(node)
            return 
        
        dic = {}
        for i,j in p:
            if j not in dic:
                dic[j] = []
            dic[j].append(i)
            

        visited = [False]*n
        curr = [False]*n
        
        for i in range(n):
            if not visited[i] and cycle(i):
                return 
            # print(visited, curr)
            
        
        visited = [False]*n
        res = deque()
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return res