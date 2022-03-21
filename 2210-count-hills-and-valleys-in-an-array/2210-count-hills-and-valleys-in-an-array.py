class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        
        arr = [nums[0]]
        
        for i in range(1,len(nums)) :
            if nums[i] != arr[-1] :
                arr.append(nums[i])
        
        
        count = 0
        for i in range(1, len(arr)-1) :
            if arr[i-1] < arr[i] > arr[i+1] :
                count += 1
            
            elif arr[i-1] > arr[i] < arr[i+1] :
                count += 1
        return count
        
        