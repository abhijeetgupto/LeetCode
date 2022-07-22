class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        dic = dict(Counter(tiles))
        
        def rec():
            
            res = 0
            for key in dic:
                if dic[key] != 0:
                    dic[key] -= 1
                    res += 1 + rec()
                    dic[key] += 1
            return res
        
        return rec()
            
        

        
#         s = set()
#         n = len(tiles)
        
#         def rec(curr = ""):
            
#             s.add(curr)
#             for i in range(n):
#                 if not visited[i]:
#                     visited[i] = True
#                     rec(curr+tiles[i])
#                     visited[i] = False
                

#         visited = [False]*n
#         rec()
#         return len(s)-1
        