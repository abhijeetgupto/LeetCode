class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = []
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    count += 1
        
        if count == 0 :
            return 0
        
        time = 0
        while queue and count>0 :
            time += 1
            nq = []
            
            def helper(row,col) :
                nonlocal count
                traverse = [(row,col-1),(row,col+1),(row-1,col),(row+1,col)]
                for l in traverse :
                    r1,c1 = l
                    if r1 in range(len(grid)) and c1 in range(len(grid[0])) and grid[r1][c1]==1 :
                        grid[r1][c1] = 2
                        count -= 1
                        nq.append([r1,c1])    
            for t in queue :
                r,c = t
                helper(r,c)

            queue = nq
        if count != 0:
            return -1
        return time
        
        
        
                    
            
            
            
        