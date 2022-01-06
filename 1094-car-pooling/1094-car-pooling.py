import sortedcontainers

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        for i in trips :
            if i[0] > capacity :
                return False
        
        trips.sort(key=lambda x:(x[1],x[2],x[0]))
        
        curr = trips[0][0]
        end = trips[0][2]
        stack = sortedcontainers.SortedList([[end,curr]])

        trips.pop(0)
        
        
        while trips :
            top = trips.pop(0)
            while stack and top[1] >= stack[0][0] :
                x = stack.pop(0)
                curr -= x[1]
            
            if top[0]+curr > capacity :
                return False
            
            else:
                stack.add([top[2],top[0]])
                curr += top[0]
                
        return True
            
            
            
        