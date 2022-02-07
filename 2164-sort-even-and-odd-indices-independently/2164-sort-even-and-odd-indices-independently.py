class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        for i  in range(len(nums)) :
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        even.sort()
        odd.sort(reverse=True)
        
        i = 0
        j = 0
        res = []
        while i<len(even) and j<len(odd) :
            res.append(even[i])
            res.append(odd[j])
            i += 1
            j += 1
        
        if i<len(even) :
            res.append(even[i])
        
        return res
        