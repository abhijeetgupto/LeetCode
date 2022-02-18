class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        
        memo  = {}
        def rec(i=row, j=col, x=k):
            if (i, j, x) in memo:
                return memo[(i, j, x)]

            if x == 1:
                count = 0
                traverse = [(i + 2, j + 1), (i + 2, j - 1), (i + 1, j + 2), (i + 1, j - 2), (i - 1, j - 2), (i - 1, j + 2),
                            (i - 2, j + 1), (i - 2, j - 1)]
                for (r, c) in traverse:
                    if r in range(n) and c in range(n):
                        count += 1
                return count

            else:
                count = 0
                traverse = [(i + 2, j + 1), (i + 2, j - 1), (i + 1, j + 2), (i + 1, j - 2), (i - 1, j - 2), (i - 1, j + 2),
                            (i - 2, j + 1), (i - 2, j - 1)]
                for (r, c) in traverse:
                    if r in range(n) and c in range(n):
                        count += rec(r, c, x - 1)
                memo[(i, j, x)] = count
                return count
            
        if k==0:
            return 1
        
        x = rec()
        return x/8**k
        
        