class Solution:
    def maximumBobPoints(self, n: int, nums: List[int]) -> List[int]:
        
        
        res = []
        memo = {}
        temp = list(range(1,12))
        
        
        def checker(arr):
            count = 0
            for idx in arr:
                count += nums[idx] + 1
            return count <= n


        def possible(i, curr, target):
            if target == 0:
                if checker(curr):
                    res.append(curr.copy())

            elif target < 0 or i >= len(temp):
                return

            else:
                for j in range(i, len(temp)):
                    possible(j + 1, curr + [temp[j]], target - temp[j])


        def rec(i=1, remaining=n):
            if len(res) >= 1:
                return

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            if i == 11:
                if remaining > nums[i]:
                    return i
                return 0

            else:
                a = rec(i + 1, remaining)
                b = 0
                if remaining > nums[i]:
                    b = i + rec(i + 1, remaining - nums[i] - 1)

                memo[(i, remaining)] = max(a, b)
                return memo[(i, remaining)]
        
        possible(0, [], rec())
        result = [0]*12
        for idx in res[0] :
            result[idx] = 1 + nums[idx]
        
        x = n-sum(result)
        if x>0 :
            result[0] = x
        
        return result
        
        
                
                    
        