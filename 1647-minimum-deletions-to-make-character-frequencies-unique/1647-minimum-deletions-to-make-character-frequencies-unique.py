class Solution:
    def minDeletions(self, s: str) -> int:
        
        arr = sorted(collections.Counter(s).values(), reverse = True)
        s = set()
        count = 0
        for val in arr:
            if val not in s:
                s.add(val)
            else:
                while val>0 and val in s:
                    val-=1
                    count+=1
                s.add(val)
        return count
        