from sortedcontainers import SortedList

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        n = len(people)
        temp = list(range(n))
        res = [0]*n
        people = sorted(people, key=lambda x: (x[0], -x[1]))
        for i in range(n):
            idx = temp.pop(people[i][1])
            res[idx] = people[i]
            
        return res
            
        