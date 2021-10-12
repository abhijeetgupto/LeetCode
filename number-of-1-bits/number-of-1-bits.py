class Solution:
    def hammingWeight(self, n: int) -> int:
        l = list(str(bin(n))[2:])

        return l.count("1")