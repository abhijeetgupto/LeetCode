class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return 
        last = nums[0]
        curr = last
        res = []

        for i in range(1, len(nums)) :
            
            if nums[i] == last+1 :
                last += 1
                
            else:
                if curr == last :
                    res.append(str(last))
                else:
                    res.append(f"{curr}->{last}")
                last = nums[i]
                curr = nums[i]
        
        if curr == last :
            res.append(str(last))
        else:
            res.append(f"{curr}->{last}")
            
        return res