class Solution:
    def readBinaryWatch(self, k: int) -> List[str]:
        
        if k >= 9 :
            return []
        
        
        hour = [1, 2, 4, 8]
        miniutes = [1, 2, 4, 8, 16, 32]
        
        h_curr = [False]*4
        m_curr = [False]*6
        
        res = set()
        
        def rec(x=0, curr = [0, 0]):
            
            if x==k:
                s = str(curr[0]) + ":"
                if len(str(curr[1])) == 1:
                    s += "0" + str(curr[1])
                else:
                    s += str(curr[1])
                res.add(s)
                return 
            
            for i,num in enumerate(hour):
                if not h_curr[i] and curr[0]+num < 12:
                    h_curr[i] = True
                    curr[0] += num
                    rec(x+1, curr)
                    h_curr[i] = False
                    curr[0] -= num
            
            for i,num in enumerate(miniutes):
                if not m_curr[i] and curr[1]+num < 60:
                    m_curr[i] = True
                    curr[1] += num
                    rec(x+1, curr)
                    m_curr[i] = False
                    curr[1] -= num
            return 
        
        rec()
        return res
            
                    
            
            
            
        
        
        