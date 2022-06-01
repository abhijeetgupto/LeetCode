class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        last = s[0]
        count = 1
        arr = []
        
        for i in range(1, len(s)):
            if s[i]==last:
                count += 1
            else:
                last = s[i]
                arr.append(count)
                count = 1
        arr.append(count)
        
        res = 0
        for i in range(len(arr)-1):
            res += min(arr[i],arr[i+1])
        
        return res
        