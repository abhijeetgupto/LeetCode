class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        temp = []
        curr = []
        curr2 = []
        count = 0
        j = 0
        
        for i in range(len(nums)) :
            if nums[i] == 0:
                if curr : 
                    temp.append([curr,curr2])
                    curr = []
                    curr2 = []
                    j = 0
            else:
                if nums[i]<0 :
                    curr2.append(j)
                j += 1
                curr.append(nums[i]*(curr[-1] if curr else 1))

        if curr :
            temp.append([curr,curr2])
        
        res = -math.inf
        for l in temp :
            if len(l[0])==1 :
                res = max(res,l[0][0])
            elif l[0][-1]>0 :
                res = max(res,l[0][-1])
            else:
                if len(l[1])==1 :
                    i = l[1][0]
                    if i==0 :
                        res = max(res, (l[0][-1])//l[0][0])
                    elif i==len(l[0])-1 :
                        res = max(res, l[0][i-1])
                    else:
                        res = max(res, l[0][-1]//l[0][i], l[0][i-1])
                else:
                    i = l[1][0]
                    j = l[1][-1]
                    if i==0 :
                        res = max(res, (l[0][-1])//l[0][0])
                    elif i==len(l[0])-1 :
                        res = max(res, l[0][i-1])
                    else:
                        res = max(res, l[0][-1]//l[0][i], l[0][i-1])
                    
                    if j==0 :
                        res = max(res, (l[0][-1])//l[0][0])
                    elif j==len(l[0])-1 :
                        res = max(res, l[0][j-1])
                    else:
                        res = max(res, l[0][-1]//l[0][j], l[0][j-1])
        if res<0 :
            if 0 in nums:
                return 0
        
        return res
                    
                
        
        
            
                
        