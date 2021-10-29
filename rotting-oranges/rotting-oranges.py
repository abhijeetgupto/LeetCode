class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        good = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
                    good += 1
                elif grid[i][j] == 2 :
                    queue.append([i,j])
                    
        if good == 0:
            return 0
        res = 0
        while queue :
            nq = []
            for r,c in queue :
                traverse = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
                for i,j in traverse :
                    if i in range(len(grid)) and j in range(len(grid[0])) and grid[i][j] == 1 :
                        good -= 1
                        grid[i][j] = 2
                        nq.append([i,j])
            if nq :        
                queue = nq
                res += 1
            else:
                break
        
        if good == 0:
            return res
        return -1
        
        