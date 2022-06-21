class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def backtrack(curr = []):
            
            if len(curr)==k:
                res.append(curr.copy())
                return 
            
            if not curr:
                for i in range(1,n+1):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
            else:
                for i in range(curr[-1]+1, n+1):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
                    
                    
        
        
        backtrack()
        return res
        