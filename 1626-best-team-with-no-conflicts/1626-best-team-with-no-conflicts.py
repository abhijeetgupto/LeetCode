class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        arr = []
        for i in range(len(ages)):
            arr.append((ages[i], scores[i]))

        arr.sort(reverse = True)
        n = len(arr)
        dp = [0]*n
        for i in range(n):
            dp[i] = arr[i][1] 
            for j in range(i):
                if arr[j][1] >= arr[i][1]:
                    dp[i] = max(dp[i], dp[j]+arr[i][1])
        
               

        return max(dp)