class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x = nums[i]*nums[j] 
                if x in dic:
                    dic[x] += 1
                else:
                    dic[x] = 1
        count = 0
        
        for key in dic:
            count += (dic[key])*(dic[key]-1)*4
        return count
                