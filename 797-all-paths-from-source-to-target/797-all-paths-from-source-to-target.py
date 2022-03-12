class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        dic = {}
        n = len(graph)
        for i in range(n) :
            dic[i] = graph[i]
        
        start = 0
        end = n-1
        
        queue = [[0,[0]]]
        res = []
        
        while queue :
            nq = []
            for node, path in queue :
                temp = dic[node]
                for key in temp :
                    if key == end:
                        res.append(path + [key])
                    elif key not in path :
                        nq.append([key, path+[key]])
            
            queue = nq
        return res