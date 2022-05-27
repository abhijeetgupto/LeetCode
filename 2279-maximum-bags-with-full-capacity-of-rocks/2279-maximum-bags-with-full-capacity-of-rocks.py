import heapq
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        temp = []
        count = 0
        for i in range(len(capacity)):
            x = capacity[i] - rocks[i]
            if x!=0:
                temp.append(x)
            else:
                count+=1
        
        temp.sort()
        for i in range(len(temp)):
            additionalRocks -= temp[i]
            if additionalRocks < 0:
                break
            count += 1
        
        return count