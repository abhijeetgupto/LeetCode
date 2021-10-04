class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p=[]
        summ=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                peri=4
                if grid[i][j]==1:
                    if j-1>=0 and grid[i][j-1]==1 :
                        peri-=1
                    if j+1<len(grid[i]) and grid[i][j+1]==1 :
                        peri-=1
                    if i-1>=0 and grid[i-1][j]==1 :
                        peri-=1
                    if i+1<len(grid) and grid[i+1][j]==1 :
                        peri-=1
                    summ+=peri
        return summ  