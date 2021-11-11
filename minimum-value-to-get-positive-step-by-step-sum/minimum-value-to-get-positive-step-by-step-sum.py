class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        p=1
        
        while True :
            x = p
            for num in nums :
                flag = 0 
                x = x + num
                if x <  1:
                    p = p+1
                    flag = 1
                    break
            if flag == 0:
                break
                
        return p