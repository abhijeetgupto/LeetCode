class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        s = set()
        n = len(tiles)
        
        def rec(curr = ""):
            
            s.add(curr)
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    rec(curr+tiles[i])
                    visited[i] = False
                

        visited = [False]*n
        rec()
        return len(s)-1
        