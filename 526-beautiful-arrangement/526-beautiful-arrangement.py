class Solution:
    def countArrangement(self, n: int) -> int:
        
        def backtrack(i = 1):
            
            if False not in visited:
                return 1
            
            res = 0
            for num in range(1, n+1):
                if not visited[num-1] and (( num%i == 0 ) or ( i%num == 0 )):
                    visited[num-1] = True
                    res += backtrack(i+1)
                    visited[num-1] = False
                    
            return res
                    
                    

        visited = [False]*n
        return backtrack()
        