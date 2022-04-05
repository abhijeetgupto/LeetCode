class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        i = 0
        j = len(height)-1
        
        while i<j :
            
            res = max(res, (j-i)*(min(height[i], height[j])))
            if height[i] > height[j] :
                j -= 1
            else:
                i += 1
        
        return res
            
        