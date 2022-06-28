class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left = 1
        right = n-2
        
        l_max = height[0]
        r_max = height[n-1]
        res = 0
        
        while left <= right:
            
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            
            if l_max < r_max:
                res += l_max - height[left]
                left+=1
                
            else:
                res += r_max - height[right]
                right -= 1
        
        return res
                