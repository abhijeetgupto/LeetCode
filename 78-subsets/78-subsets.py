class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        def rec(curr = [[]], i = 0):
            
            if i >= n:
                return curr
            
            else:
                temp = []
                for element in curr :
                    temp.append(element)
                    temp.append(element+[nums[i]])
                
                return rec(temp, i+1)
        
        return rec()
                    
            
 