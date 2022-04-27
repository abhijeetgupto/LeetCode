class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        parent = list(range(len(points)))
        
        def find(x):
            if parent[x] == x :
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        
        graph = []
        for i in range(len(points)):
            x1,y1 = points[i][0],points[i][1]
            for j in range(i+1, len(points)):
                x2,y2 = points[j][0],points[j][1]
                graph.append(((abs(x1-x2) + abs(y1-y2)),i,j))
                
        graph.sort()
        count = 0
        
        for w,i,j in graph :
            x1 = find(i)
            x2 = find(j)
            if x1 != x2 :
                parent[x1] = x2
                count += w
                
        return count
                
            
            
        
        