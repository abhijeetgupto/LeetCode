class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(x):    
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def unite(i, j):   
            s1 = find(i)
            s2 = find(j)
            if s1 == s2:
                return True
            else:
                if rank[s1] < rank[s2]:
                    parent[s1] = s2
                    rank[s2] += rank[s1]
                else:
                    parent[s2] = s1
                    rank[s1] += rank[s2]
                return False
                    
        
        parent = [-1]*len(edges)
        rank = [1]*len(edges)
        
        for i,j in edges:
            if unite(i-1, j-1):
                return [i,j]
            
        