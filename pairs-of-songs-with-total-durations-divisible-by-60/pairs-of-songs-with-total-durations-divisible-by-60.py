class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        time.sort()
        m = max(time)
        dic = dict(collections.Counter(time))
        
        count = 0
        
        for key in dic :
            
            if (2*key)%60 == 0:
                count += (dic[key])*(dic[key]-1)//2
                
            k = key%60
            k = 60-k
            
            while k <= key:
                k += 60
                
            while k <= m :
                if k in dic :
                    count += dic[k]*dic[key]
                k += 60
                
        return count
                    
            
                
            
            
        