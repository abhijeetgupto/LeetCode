class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        count = 0
        
        while people :
            top = people.pop(0)
            x = limit-top
            if people : 
                if x == 0 :
                    count += 1

                else:
                    idx = bisect.bisect_left(people, x)

                    if idx == len(people) :
                        people.pop(idx-1)
                        count += 1

                    elif people[idx] == x :
                        people.pop(idx)
                        count += 1

                    else:
                        if idx == 0 :
                            count += 1
                        else:
                            people.pop(idx-1)
                            count += 1
            else:
                count+=1
        return count
        
        