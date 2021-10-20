class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        while "" in s :
            s.remove("")
        s.reverse()
        return " ".join(s)
        