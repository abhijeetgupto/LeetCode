from sortedcontainers import SortedSet

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        visited = SortedSet([rating[0]])
        to_visit = SortedSet(rating[1:])
        
        count = 0
        for i in range(1, len(rating)) :
            
            x = rating[i]
            visited.add(x)
            idx1 = bisect.bisect_left(visited, x)
            idx2 = bisect.bisect_left(to_visit, x)
            
            count += idx1*(len(to_visit)-idx2-1)
            count += idx2*(len(visited) -idx1-1)
            to_visit.remove(x)
        
        return count
            
            