class Solution:
    def toHex(self, num: int) -> str:
        
        dic = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        
        if num<0 :  
            num += 2**32
            
        if num==0:
            return "0"
        
        res = ""
        while num :
            
            re = num%16
            if re<10 :
                res += str(re)
            else:
                res += dic[re]
            num = num//16
        
        return res[::-1]
                
        