class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        
        def solve(x, x_b) : 
            
            count = 0
            if len(x) == 1 :
                if x == "0" :
                    count = 0
                    curr = startAt
                else:
                    s1 = x[0]
                    if int(s1) != startAt :
                        count += moveCost + pushCost
                        curr = int(s1)
                    else:
                        count += pushCost
                        curr = startAt
                        
            else:
                s1 = x[0]
                s2 = x[1]
                if int(s1) != startAt :
                    count += moveCost + pushCost
                    curr = int(s1)
                else:
                    count += pushCost
                    curr = startAt

                if int(s2) != curr :
                    count += moveCost + pushCost
                    curr = int(s2)
                else:
                    count += pushCost


            if len(x_b) == 1 :
                if x_b == "0" :
                    if curr == 0 :
                        count += 2*pushCost
                    else:
                        count += 2*pushCost
                        count += moveCost
                else:
                    
                    
                    if curr != 0 :
                        count += moveCost
                        count += pushCost
                        curr = 0
                    else:
                        count += pushCost

                    
                    if curr == int(x_b):
                        count += (pushCost+moveCost)
                    else:
                        count += pushCost
                        count += moveCost

            else:
                s1 = x_b[0]
                s2 = x_b[1]
                if int(s1) != curr :
                    count += moveCost + pushCost
                    curr = int(s1)
                else:
                    count += pushCost

                if int(s2) != curr :
                    count += moveCost + pushCost
                    curr = int(s2)
                else:
                    count += pushCost
            return count

        if targetSeconds < 60 :
            temp = str(targetSeconds)
            if len(temp)==1 :
                if targetSeconds == startAt :
                    return pushCost
                else:
                    return pushCost+moveCost
            
            else:
                
                curr = startAt
                res = 0 
                if int(temp[0]) == curr :
                    res += pushCost
                else:
                    res += moveCost+pushCost
                    curr = int(temp[0])
                
                if int(temp[1]) == curr :
                    res += pushCost
                else:
                    res += moveCost+pushCost
                    curr = int(temp[1]) 
                
                
                return res
                
                
                
        x1 = targetSeconds//60
        x2 = targetSeconds - x1*60
        
        
        
        if x1 != 0 and x2+60 < 100 and x1 < 100:
            return min(solve(str(x1),str(x2)), solve(str(x1-1), str(x2+60)))
        
        else:
            if x1 == 0 :
                temp = str(targetSeconds)
                if len(temp)==1 :
                    if targetSeconds == startAt :
                        return pushCost
                    else:
                        return pushCost+moveCost
                else:

                    curr = startAt
                    res = 0 
                    if int(temp[0]) == curr :
                        res += pushCost
                    else:
                        res += moveCost+pushCost
                        curr = int(temp[0])

                    if int(temp[1]) == curr :
                        res += pushCost
                    else:
                        res += moveCost+pushCost
                        curr = int(temp[1]) 


                    return res
                
            elif x1>99 :
                return solve(str(x1-1), str(x2+60))
            
            else:
                return solve(str(x1),str(x2))
            
        