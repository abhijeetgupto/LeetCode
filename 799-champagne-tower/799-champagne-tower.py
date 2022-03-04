class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        dp = [[poured]]
        
        for i in range(1, query_row+1) :
            temp = []
            for j in range(len(dp[-1])+1) :
                
                if j == 0:
                    temp.append(max(0,(dp[-1][0]-1)/2))
                    
                elif j == len(dp[-1]) :
                    temp.append(max(0,(dp[-1][0]-1)/2))
                
                else:
                    x1 = max(0, (dp[-1][j-1]-1)/2)
                    x2 = max(0, (dp[-1][j]-1)/2 )
                    temp.append(x1+x2)
                    
            dp.append(temp)

        return min(1, dp[query_row][query_glass])
                    
        
        
        
        