class Solution:
    def shipWithinDays(self, arr: List[int], days: int) -> int:
        
        def checker(x,days) :
            d = 0
            curr = 0
            falg = False
            
            for i in range(len(arr)):
                if curr + arr[i] <= x :
                    flag = False
                    curr += arr[i]
                else:
                    flag = True
                    curr = arr[i]
                    d += 1
                    
            return d+1 <= days
            
            
        m = max(max(arr),math.ceil(sum(arr)/days))
        while True :
            if checker(m,days) :
                return m
            else:
                m += 1
                