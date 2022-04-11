class Solution:
    def originalDigits(self, s: str) -> str:
        
        
        res = [0]*10
        
        res[0] = s.count('z')
        res[4] = s.count('u')
        res[2] = s.count('w')
        res[8] = s.count('g')
        res[6] = s.count('x')
        res[3] = s.count('r') - res[0] - res[4]
        res[7] = s.count('s') - res[6]
        res[5] = s.count('v') - res[7]
        res[1] = s.count('o') - res[0] - res[2] - res[4] 
        res[9] = (s.count('n') - res[1] -res[7])//2
        
        ans = ""
        for i in range(10) :
            ans += str(i)*res[i]
        
        return ans
        
        
        
        