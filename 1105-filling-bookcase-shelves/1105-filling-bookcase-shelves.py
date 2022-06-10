from functools import lru_cache
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        n = len(books)
        
        @lru_cache(None)
        def rec(i=0, curr=0, m=0):
            
            if i>=n:
                return m
            
            if curr + books[i][0] <= shelfWidth:
                a = rec(i+1, curr+books[i][0], max(m, books[i][1]))
                b = m + rec(i+1, books[i][0], books[i][1])
                return min(a, b)
                
            else:
                return m + rec(i+1, books[i][0], books[i][1])
        
        return rec()
                
      