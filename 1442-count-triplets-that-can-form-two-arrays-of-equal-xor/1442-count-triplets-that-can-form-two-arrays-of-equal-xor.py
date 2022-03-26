from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])

        n = len(prefix)
        count = 0
        for j in range(1, n):
            d1 = defaultdict(int)
            for k in range(j, n):
                d1[prefix[k] ^ prefix[j - 1]] += 1

            d2 = defaultdict(int)
            for i in range(j):
                if i == 0:
                    x = prefix[j - 1]
                else:
                    x = prefix[i - 1] ^ prefix[j - 1]
                d2[x] += 1

            for key in d1:
                if key in d2:
                    count += (d1[key] * d2[key])

        return count

       