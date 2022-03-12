from sortedcontainers import SortedList


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        dic = {}
        for i in range(n) :
            for j in range(n) :
                if i!=j and isConnected[i][j]==1 :
                    
                    if i not in dic :
                        dic[i] = set()
                    if j not in dic :
                        dic[j] = set()

                    dic[i].add(j)
                    dic[j].add(i)

        l = SortedList(range(n))

        res = 0
        while l :
            res += 1
            top = l.pop()
            queue = [top]
            visited  = set()
            while queue :
                nq = []
                for node in queue :
                    if node not in visited :
                        if node in dic :
                            nq += dic[node]
                        visited.add(node)

                    if node in l : 
                        l.remove(node)
                queue = nq
                    
        return res
            
            
                
            
                    
            
            
        
                
        