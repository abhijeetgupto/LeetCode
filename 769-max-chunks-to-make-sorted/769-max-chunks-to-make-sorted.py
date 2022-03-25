from sortedcontainers import SortedList

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        chunk = SortedList()
        expected = SortedList()
        count = 0
        x = 0

        for i in range(len(arr)) :
            
            chunk.add(arr[i])
            expected.add(x)
            
            x+=1
            if chunk == expected :
                count += 1
                chunk = SortedList()
                expected = SortedList()
                
        if chunk :
            count+=1
        return count
            
            
            
        