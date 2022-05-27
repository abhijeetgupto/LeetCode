from fractions import Fraction
class Solution:
    def minimumLines(self, arr: List[List[int]]) -> int:
        
        
        
        if len(arr)==1:
            return 0
        
        if len(arr)==2:
            return 1
        
        arr.sort()
        count = 1
        curr_m = Fraction((arr[1][1]-arr[0][1]),(arr[1][0]-arr[0][0]))
        for i in range(2, len(arr)):
            m = Fraction((arr[i][1]-arr[i-1][1]),(arr[i][0]-arr[i-1][0]))
            if m != curr_m:
                count += 1
                curr_m = m
        
        return count
                
            
        
        