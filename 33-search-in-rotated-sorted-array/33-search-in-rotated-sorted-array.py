class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        s = 0
        e = len(nums)-1
        
        while s <= e:

            m = (s + e) // 2
            right = nums[e]
            left = nums[s]
            mid = nums[m]
            

            if mid == target:
                return m

            if right > mid:
                #right part of the array is sorted
                if target > mid and target <= right :
                    s = m+1
                else:
                    e = m-1
                    
            else:
                #left part of array is sorted
                if target >= left and target < mid :
                    e = m-1
                else:
                    s = m+1
                
        return -1

                    
                
                    
        