class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        left = [0]
        right = [0]
        curr = 0
        for num in nums:
            curr+=num
            left.append(curr)
        
        if curr<x:
            return -1
        
        if curr == x:
            return len(nums)
        
        curr = 0
        for i in range(len(nums)-1,-1,-1):
            curr += nums[i]
            right.append(curr)

        res = math.inf
        for i in range(len(left)):
            y = x - left[i]
            if y<0:
                break
            idx = bisect.bisect_left(right, y)
            
            if idx in range(len(left)-i) and right[idx] == y:
                res = min(res, idx+i)
        
        if res==math.inf:
            return -1
        return res
        
        
        
        
        
        