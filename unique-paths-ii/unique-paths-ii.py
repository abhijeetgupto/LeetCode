class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def ways(mat, i, j, memo={}):
            if (i, j) in memo:
                return memo[(i, j)]

            elif i == len(mat) - 1 and j == len(mat[0]) - 1:
                if mat[i][j] == 0:
                    return 1
                else:
                    return 0
            elif i == len(mat) - 1:

                while j < len(mat[0]):
                    if mat[i][j] != 0:
                        return 0
                    j += 1
                return 1

            elif j == len(mat[0]) - 1:
                while i < len(mat):
                    if mat[i][j] != 0:
                        return 0
                    i += 1
                return 1

            else:
                if mat[i][j] == 0:
                    memo[(i, j)] = ways(mat, i + 1, j) + ways(mat, i, j + 1)
                    return memo[(i, j)]
                else:
                    return 0
        return ways(obstacleGrid,0,0)
    