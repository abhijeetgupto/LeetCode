class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        
        def dfs(x, y, r, curr):
            res = 0
            for i in range(n):
                if i not in curr and checker(x, y, r, bombs[i][0], bombs[i][1], bombs[i][2]):
                    curr.add(i)
                    res += 1 + dfs(bombs[i][0], bombs[i][1], bombs[i][2],curr)
            return res
                
                
        
        def checker(x1, y1, r1, x2, y2, r2):
            return ((x1-x2)**2 + (y1-y2)**2)**0.5 <= r1
            
            

        res = 0
        n = len(bombs)
        bombs.sort()
        for i in range(n):
            res = max(res, 1+dfs(bombs[i][0], bombs[i][1], bombs[i][2], {i}))
        
        return res
        