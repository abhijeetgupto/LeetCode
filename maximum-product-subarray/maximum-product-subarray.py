class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def helper(arr) :
            
            if len(arr)==1:
                return arr[0]
            
            n = 0
            for num in arr :
                if num<0:
                    n += 1
                    
            res = 1
            for num in arr:
                res*=num
                
            if n%2 == 0:
                return res
            else:
                curr = 1
                m = 0
                for i in range(len(arr)):
                    curr*=arr[i]
                    if arr[i]<0 :
                        m = max(m, curr//arr[i], res//curr)
                return m
        
        if len(nums)==1:
            return nums[0]
        
        l  = []
        temp = []
        
        while nums :
            top = nums.pop(0)
            if top == 0 :
                if temp : 
                    l.append(temp)
                    temp = []
            else:
                temp.append(top)
        if temp :
            l.append(temp)
        
        res = 0
        for arr in l :
            res = max(res, helper(arr))
            
        return res
                        
                
                
        