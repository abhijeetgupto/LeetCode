class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        index = []
        for i in range(len(nums)) :
            if nums[i]%2 != 0:
                index.append(i)
        
        if len(index) < k :
            return 0
        
        i = 0
        j = k-1
        res = 0
        
        while j < len(index) :
            
            if i == 0 and j == len(index)-1 :
                return (index[i]+1)*(len(nums)-index[j])
            
            elif i == 0 :
                res += (index[i]+1)*(index[j+1] - index[j])
            
            elif j == len(index)-1 :
                res += (index[i] - index[i-1])*(len(nums)-index[j])
            
            else:
                res += (index[i] - index[i-1])*(index[j+1] - index[j])
                
            i += 1
            j += 1
            
        return res
        
        
            
            