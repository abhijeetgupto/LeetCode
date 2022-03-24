class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        
        def checker(k) :
            
            curr = k
            count = 0
            last = 0
            i=0
            
            while i<len(batteries) :
                
                if last+batteries[i] < curr :
                    curr -= batteries[i]+last
                    i += 1
                    last = 0
                
                elif curr == batteries[i]+last :
                    count += 1
                    curr = k
                    i+=1
                    last = 0
                
                else:
                    last = batteries[i] + last -curr
                    count += 1
                    curr = k
                    i+=1
            return count >= n
        
                
        
        if len(batteries) == n :
            return min(batteries) 
        
        if n==1 :
            return sum(batteries)
        
        batteries.sort()
        s = 0
        e = sum(batteries)//n
        res = s
        
        while s<=e :
            
            m = (s+e)//2
            if checker(m) :
                s = m+1
                res = m
                
            else:
                e = m-1
                
        return res
                
                
                
    