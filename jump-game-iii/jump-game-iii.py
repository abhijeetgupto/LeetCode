class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        visited = set()
        stack = [start]
        
        while stack :
            
            nq = []
            for idx in stack :
                if arr[idx] == 0:
                    return True
                
                visited.add(idx)
                x = idx + arr[idx]
                y = idx - arr[idx]
                
                if x not in visited and x < n and x >=0 :
                    nq.append(x)
                
                if y not in visited and y < n and y >=0 :
                    nq.append(y)
            stack = nq
            
        return False
                
                
        
        