from sortedcontainers import SortedList
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        arr = SortedList()
        curr = []
        
        while i >= 0 :
            
            arr.add(nums[i])
            curr.append(nums[i])
            
            if curr == arr :
                i -= 1
            
            else:
                x = curr.pop()
                idx = bisect.bisect_right(arr, x)
                if arr[idx] == x :
                    idx += 1
                    
                y = arr.pop(idx)
                nums[:] = nums[: i] + [y] + list(arr)
                break
        if i==-1 :
            nums.sort()
                
            
        
                
                
            
         