class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        temp = []
        curr = []
        count = 0
        for i in range(len(nums)) :
            if nums[i] == 0:
                if curr : 
                    temp.append([curr,count])
                    curr = []
                    count = 0
            else:
                if nums[i]<0 :
                    count +=  1
                curr.append(nums[i])
        if curr :
            temp.append([curr,count])
            
        res = 0
        for l in temp :
            if l[1]%2 == 0:
                res = max(res, len(l[0]))
            else:
                x = 0
                y = 0
                for i in range(len(l[0])) :
                    x += 1
                    if l[0][i] < 0:
                        break
                    
                for i in range(len(l[0])-1,-1,-1) :
                    y += 1
                    if l[0][i] < 0:
                        break
                    
                t = min(x, y)
                res = max(res, len(l[0])-t)
        return res
    
                
        
            
                
            
            
       