class Solution:
    def bitwiseComplement(self, num: int) -> int:
        binary = (bin(num))[2:]
        binary = list(binary)
        compliment = ''.join('1' if x == '0' else '0' for x in binary)
        return int(compliment , 2)
    
        
        