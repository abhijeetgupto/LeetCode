class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s
        
        n = len(s)
        numCols = (math.ceil(n / (2 * numRows - 2)))*(numRows-1)
        mat = [["" for _ in range(numCols)] for _ in range(numRows)]
        
        currCol = 0
        i = 0
        while i < len(s):

            j = 0
            while i < n and j < numRows:
                mat[j][currCol] = s[i]
                i += 1
                j += 1

            currCol += 1
            j = numRows - 2
            while i < n and j > 0:
                mat[j][currCol] = s[i]
                i += 1
                j -= 1
                currCol += 1
                
        res = ""
        for l in mat :
            res += "".join(l)
        
        return res

        