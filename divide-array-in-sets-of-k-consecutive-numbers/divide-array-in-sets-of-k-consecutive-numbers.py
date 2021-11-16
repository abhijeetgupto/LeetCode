class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums)%k!= 0:
            return False
        
        dic = dict(collections.Counter(nums))
        
        while dic :
            
            m = min(dic.keys())
            x = dic[m]
            
            for i in range(m,m+k):
                if i not in dic or dic[i] < x:
                    return False
                else:
                    dic[i] -= x
                    if dic[i] == 0 :
                        dic.pop(i)
        return True