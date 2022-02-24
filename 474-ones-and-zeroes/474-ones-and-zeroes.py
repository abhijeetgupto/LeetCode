class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        l = len(strs)
        memo = {}
        
        def rec(i=0, zeros=0, ones=0) :
            
            if zeros > m or ones > n :
                return -1
            
            if (i, zeros, ones) in memo:
                return memo[(i,zeros,ones)]
            
            if i >= l :
                return 0
                        
            else:
                memo[(i,zeros,ones)] = max(1+rec(i+1, zeros+temp[i][0], ones+temp[i][1]), rec(i+1, zeros, ones))
                return memo[(i,zeros,ones)]
            
        
        temp = []
        for s in strs :
            x = []
            x.append(s.count('0'))
            x.append(len(s)-x[0])
            temp.append(x)
            
        return rec()