class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        
        
        def cycle(node):
            
            visited[node] = True
            curr[node] = True
            for nbr in dic[node]:
                if not visited[nbr]:
                    if cycle(nbr):
                        return True
                elif curr[nbr]:
                    return True
            curr[node] = False
            return False
            
   
        dic = defaultdict(list)
        for i,j in p:
            dic[j].append(i)
        
        
        curr = [False]*n
        visited = [False]*n
        for node in range(n):
            if not visited[node] and cycle(node):
                return False
            
        return True
        
        