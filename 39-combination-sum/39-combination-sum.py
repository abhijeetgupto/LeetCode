import sortedcontainers
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def rec(k=target, curr=None):

            if curr is None:
                curr = defaultdict(int)

            if k == 0:
                temp = sortedcontainers.SortedList([])

                for key in curr:
                    for _ in range(curr[key]):
                        temp.add(key)
                if temp not in res:
                    res.append(temp)

            elif k < 0:
                return

            else:
                for num in candidates:
                    curr[num] += 1
                    rec(k - num, curr)
                    curr[num] -= 1

        rec()
        return res