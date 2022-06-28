class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        right = [0]*n
        right[n-1] = height[n-1]
        
        for i in range(n-2,-1,-1):
            right[i] = max(height[i], right[i+1])
        
        l_max = height[0]
        res = 0
        
        for i in range(1, n-1):
            l_max = max(l_max, height[i])
            res += min(l_max, right[i]) - height[i]
        
        return res   