class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        for i in range(1,rowIndex+2):
            l.append([1]*i)
        
        x=[1,1]
        for i in range(2,len(l)):
            for j in range(1,len(l[i])-1):
                l[i][j] = x[j-1] + x[j]    
            x = l[i]  
            
        return l[-1]
        