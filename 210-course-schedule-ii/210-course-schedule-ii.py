class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:

        def dfs(node):
            visited[node] = True
            curr[node] = True
            if node in dic:
                for nbr in dic[node]:
                    if not visited[nbr]:
                        if dfs(nbr):
                            return True
                    elif curr[nbr]:
                        return True
                        
            curr[node] = False
            res.appendleft(node)
            return False
        
        dic = {}
        for i,j in p:
            if j not in dic:
                dic[j] = []
            dic[j].append(i)
            

        curr = [False]*n  
        visited = [False]*n
        res = deque()
        
        for i in range(n):
            if not visited[i]:
                if dfs(i):
                    return 
        
        return res