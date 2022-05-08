from sortedcontainers import SortedList

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        if ladders == 0:
            
            for i in range(1, len(heights)):
                if heights[i]-heights[i-1]>0:
                    bricks -= heights[i]-heights[i-1]
                
                if bricks < 0 :
                    return i-1
            return i
                
            
        
        temp = []
        for i in range(1, len(heights)):
            x = heights[i] - heights[i - 1]
            if x > 0:
                temp.append([x, i])
        
        if not temp or ladders >= len(temp) :
            return len(heights)-1
        

        ladders_arr = SortedList()
        for i in range(ladders):
            ladders_arr.add(temp[i][0])
        

        bricks_arr = SortedList()
        for i in range(ladders, len(temp)):
            x = temp[i][0]
            if x < ladders_arr[0]:
                bricks_arr.add(x)
                bricks -= x
            else:
                t = ladders_arr[0]
                bricks_arr.add(t)
                ladders_arr.remove(t)
                ladders_arr.add(x)
                bricks -= t
            if bricks == 0:
                break
            elif bricks < 0:
                i -= 1
                break

        idx = temp[i][1]
        for i in range(idx+1, len(heights)):
            if heights[i] <= heights[i-1]:
                idx+=1
            else:
                break
                
        return idx
        
        
  

        
        
            
                
            
        