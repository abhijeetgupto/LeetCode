class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = [[-a,"a"],[-b,"b"],[-c,"c"]]
        heapq.heapify(heap)
        
        s = ""
        while heap :
            
            x = heapq.heappop(heap)
            if x[0] == 0 :
                break
            char = x[1]
            
            if len(s) >= 2 :
                
                if s[-1] == char and s[-2] == char :
                    if heap : 
                        temp = heapq.heappop(heap)
                        if temp[0] == 0:
                            break
                        else:
                            heapq.heappush(heap,x)
                            s += temp[1]
                            temp[0] += 1
                            if temp[0] != 0 :
                                heapq.heappush(heap,temp)
                    else:
                        break
   
                else:
                    s += char
                    x[0] += 1
                    if x[0] != 0 :
                        heapq.heappush(heap,x)

            else :
                s += char
                x[0] += 1
                if x[0] != 0 :
                    heapq.heappush(heap,x)
        return s