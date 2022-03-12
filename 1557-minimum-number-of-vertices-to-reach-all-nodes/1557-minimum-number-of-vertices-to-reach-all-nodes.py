class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        dic = {}
        
        for fr,to in edges :
            if fr in dic :
                dic[fr].add(to)
            else:
                dic[fr] = {to}
        
        l = set(range(n))
        for key in dic :
            for node in dic[key] :
                if node in l :
                    l -= {node}
        
        return l
        