class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        
        out = [[1],[1,1]]
        for rows in range(3,numRows+1):
            l = []
            l.append(1)
            
            for i in range(len(out[-1])-1):
                l.append(out[-1][i] + out[-1][i+1])
            
            l.append(1)
            out.append(l)
        
        return out
            