class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        temp = []
        curr = 0
        for num in differences :
            curr += num
            temp.append(curr)
        
        mi = min(0,min(temp))
        ma = max(0,max(temp))
        x1 = lower- mi
        x2 = upper- ma
        
        if x2-x1+1>0:
            return x2-x1+1
        return 0
        