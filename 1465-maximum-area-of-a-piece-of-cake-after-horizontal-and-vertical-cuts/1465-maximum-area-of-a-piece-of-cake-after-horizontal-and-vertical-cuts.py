class Solution:
    def maxArea(self, h: int, w: int, h1: List[int], v1: List[int]) -> int:
        
        m = (10**9) +7
        
        h1.sort()
        v1.sort()
        
        h1.insert(0, 0)
        v1.insert(0, 0)
        
        h1.append(h)
        v1.append(w)
        
        m1 = m2 = 0
        for i in range(1, len(h1)):
            m1 = max(m1, h1[i]-h1[i-1])
        
        for i in range(1, len(v1)):
            m2 = max(m2, v1[i]-v1[i-1])
        
        return ((m1%m)*(m2%m))%m