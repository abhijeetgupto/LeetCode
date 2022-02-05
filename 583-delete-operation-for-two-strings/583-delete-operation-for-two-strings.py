class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def rec(s1, s2, i, j, memo={}):

            if (i, j) in memo:
                return memo[(i, j)]

            elif i < len(s1) and j < len(s2):
                
                if s1[i] == s2[j]:
                    memo[(i,j)] = rec(s1, s2, i + 1, j + 1, memo)
                    return memo[(i,j)]

                else:
                    x1 = 1 + rec(s1, s2, i + 1, j, memo)
                    x2 = 1 + rec(s1, s2, i, j + 1, memo)
                    x3 = 2 + rec(s1, s2, i + 1, j + 1, memo)
                    memo[(i, j)] = min(x1, x2, x3)
                    return memo[(i, j)]
                
            else:
                if i >= len(s1) and j >= len(s2):
                    return 0

                elif i >= len(s1):
                    return len(s2) - j

                else:
                    return len(s1) - i

        return rec(word1, word2, 0,0)