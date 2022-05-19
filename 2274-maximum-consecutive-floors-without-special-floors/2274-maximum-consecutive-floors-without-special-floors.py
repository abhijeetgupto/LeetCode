class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        res = 0
        special.sort()
        temp = [bottom]
        for num in special:
            if num >= temp[-1]:
                temp.append(num)
            if num>=top:
                break
                
        temp.append(top)
        
        for i in range(1, len(temp)):
            if i == 1 and bottom not in special:
                res = max(res, temp[i]-temp[i-1])
            
            elif i==len(temp)-1 and top not in special:
                res = max(res, temp[i]-temp[i-1])
            else:    
                res = max(res, temp[i]-temp[i-1]-1)
        
        return res
        