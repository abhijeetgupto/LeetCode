class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        dp = [[0]*(len(mat[0])+1)]
        for i in range(len(mat)):
            temp = [0]
            for j in range(len(mat[0])):
                temp.append(temp[-1] + dp[-1][j+1] + mat[i][j] - dp[-1][j])
            dp.append(temp)
        
        
        def checker(k):
            
            for i in range(1, len(dp)-k+1):
                for j in range(1, len(dp[0])-k+1):
                    s = dp[i+k-1][j+k-1] -dp[i+k-1][j-1] -dp[i-1][j+k-1] + dp[i-1][j-1]
                    if s <= threshold:
                        return True
            return False
        
        s = 0
        e = min(len(mat), len(mat[0]))
        res = 0
        
        while s <= e:
            
            mid = (s+e)//2
            if checker(mid):
                res = mid
                s = mid+1
            else:
                e = mid-1
        
        return res
                
            
                
        