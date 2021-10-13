class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:]
        x = x[::-1]
        if len(x) < 32:
            temp = 32-len(x)
            x += "0"*temp
        x = int(x,2)
        return x
        
        