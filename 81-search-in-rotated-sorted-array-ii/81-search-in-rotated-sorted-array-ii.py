class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        s = 0
        e = len(nums)-1
        
        while s<=e :
            
            while s<e and nums[s] == nums[s+1]:
                s+=1
                
            while s<e and nums[e] == nums[e-1]:
                e-=1
            
            
            m = (s+e)//2
            
            left = nums[s]
            right = nums[e]
            mid = nums[m]
            
            if target == mid :
                return True
            
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
                    
        return False
            
           
            
        