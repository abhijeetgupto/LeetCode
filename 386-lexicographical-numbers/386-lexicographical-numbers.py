class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        l = [str(i) for i in range(1, n+1)]
        l.sort()
        l = [int(i) for i in l]
        return l