class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        count = 0
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < last:
                count += 1
                last = min(intervals[i][1], last)
                
            else:
                last = intervals[i][1]
                
        return count
            
            
        