class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        final = []
        visited = set()
        
        def twosum(nums, target) :
            memo = set()
            res = []
            for num in nums :
                x = target-num
                if x in memo :
                    temp = [num,x,-target]
                    temp.sort()
                    check = str(temp[0])+","+str(temp[1])+","+str(temp[2])
                    if check not in visited :
                        final.append(temp)
                        visited.add(check)
                    
                memo.add(num)

                
        for i in range(len(nums)-1) :
            twosum(nums[i+1:],-nums[i])
        
        return final