from sortedcontainers import SortedList
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curr = 0
        dic= defaultdict(int)
        s = SortedList()
        prefix = []
        
        for num in nums :
            curr += num
            s.add(curr)
            prefix.append(curr)
        
        count = prefix.count(k)
        
        for i in range(len(prefix)):
            s.remove(prefix[i])
            t = k+prefix[i]
            count += s.count(t)
        
        return count
            
        
        
        
      
        
        
        