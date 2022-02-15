class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()
        dic = dict(collections.Counter(beans))
        prefix = []
        curr = 0
        
        for key in dic:
            curr += dic[key] * key
            prefix.append(curr)

        n = len(beans) - dic[beans[0]]
        ans = (prefix[-1] - prefix[0]) - (beans[0] * n)
        i = 0
        for key in dic:
            if i == 0:
                i += 1
            else:
                n -= dic[key]
                ans = min(prefix[i - 1] + (prefix[-1] - prefix[i] - key * n), ans)
                i += 1
                
        return ans