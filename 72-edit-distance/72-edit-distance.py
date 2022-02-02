class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
 
        # recursion
        
        def rec(s1, s2, i, j, memo={}):
            n1 = len(s1)
            n2 = len(s2)

            if (i, j) in memo:
                return memo[(i, j)]

            elif i >= n1 and j >= n2:
                return 0

            elif i >= n1 or j >= n2:

                if i >= n1:
                    return n2 - j
                else:
                    return n1 - i
            else:
                if s1[i] == s2[j]:
                    return rec(s1, s2, i + 1, j + 1, memo)

                else:
                    a = rec(s1, s2, i + 1, j + 1, memo)
                    b = rec(s1, s2, i + 1, j, memo)
                    c = rec(s1, s2, i, j + 1, memo)

                    memo[(i, j)] = 1 + min(a, b, c)
                    return memo[(i, j)]
        
        return rec(word1,word2,0,0)