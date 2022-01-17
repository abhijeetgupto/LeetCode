class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        dic = dict(collections.Counter(nums))
        arr = sorted(dic.keys())
        n = len(arr)
        
        taken = arr[n-1]*dic[arr[n-1]]
        not_taken = 0
        
        for i in range(n-2,-1,-1) :
            
            if arr[i]+1 == arr[i+1] :
                temp = not_taken + arr[i]*dic[arr[i]]
                not_taken = max(taken, not_taken)
                taken = temp
                
            else:
                temp = max(taken, not_taken) + arr[i]*dic[arr[i]]
                not_taken = max(taken, not_taken)
                taken = temp
        
        return max(taken, not_taken)
            
        
            
        
        
        
        
        
        
        
             
        
                        
                    
                
                
                
        
        
            
            
            
        
        
        