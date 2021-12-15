class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        x = math.ceil((((1 + 8*n)**(0.5))-1)/2)
        return x
        