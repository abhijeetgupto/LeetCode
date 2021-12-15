class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        
        n = len(m)
        if n==1 :
            return m[0][0]
        
        m1 = m[0][0]
        m2 = m[0][1]
        if m1 > m2 :
            l = [[m2,1],[m1,0]]
        else:
            l = [[m1,0],[m2,1]]
        
        for i in range(2,n) :
            val = m[0][i]
            if val <= l[0][0] :
                l[1] = l[0]
                l[0] = [val,i]
                
            elif val < l[1][0] :
                l[1] = [val,i]
                
        
        
        for i in range(1,n) :
            for j in range(n) :
                if j != l[0][1] :
                    m[i][j] += l[0][0]
                else:
                    m[i][j] += l[1][0]
                    
            m1 = m[i][0]
            m2 = m[i][1]
            if m1 > m2 :
                l = [[m2,1],[m1,0]]
            else:
                l = [[m1,0],[m2,1]]

            for j in range(2,n) :
                val = m[i][j]
                if val <= l[0][0] :
                    l[1] = l[0]
                    l[0] = [val,j]

                elif val < l[1][0] :
                    l[1] = [val,j]
                    
        return min(m[-1])
            
                
            
                
            
        
        