from sortedcontainers import SortedList

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        chunk = SortedList()
        expected = SortedList()
        count = 0
        temp = sorted(arr, reverse= True)

        for i in range(len(arr)) :
            
            chunk.add(arr[i])
            expected.add(temp.pop())
            
            
            if chunk == expected :
                count += 1
                chunk = SortedList()
                expected = SortedList()
                
        if chunk :
            count+=1
        return count