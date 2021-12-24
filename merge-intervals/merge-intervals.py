class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        
        last = intervals.pop(0)
        
        while intervals :
            top = intervals.pop(0)
            if top[0] <= last[1]:
                last = [last[0], max(last[1],top[1])]
            else:
                res.append(last)
                last = top
        res.append(last)        
        return res