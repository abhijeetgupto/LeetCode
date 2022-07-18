from sortedcontainers import SortedList
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curr = 0
        dic = defaultdict(int)
        prefix = []
        
        for num in nums :
            curr += num
            dic[curr] += 1
            prefix.append(curr)
        
        count = prefix.count(k)
        
        for i in range(len(prefix)):
            dic[prefix[i]] -= 1
            t = k+prefix[i]
            count += dic[t]
        
        return count
            
        
        
        
      
        
        
        