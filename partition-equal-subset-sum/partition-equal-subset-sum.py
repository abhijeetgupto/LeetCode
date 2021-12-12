class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def fun(arr,target,curr = set(),dic = {}) :
            
            if target == 0:
                return True
            
            if target < 0 :
                return False
            
            if len(curr) == len(nums) :
                return False
            
            if target in dic :
                return dic[target]
            
            for i in range(len(arr)) :
                if i not in curr : 
                    x = fun(arr,target-arr[i],curr.union({i}))
                    if x :
                        return True
                    else:
                        dic[target] = False
                    
            dic[target] = False
 
        s = sum(nums)
        if s%2 != 0 :
            return False
        
        target = s//2
        return fun(nums,target)
        
        
            
            
        
        
        