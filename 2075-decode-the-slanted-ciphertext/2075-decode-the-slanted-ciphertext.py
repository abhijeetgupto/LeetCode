class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        if not encodedText:
            return ""
        
        matrix = []
        n = len(encodedText)
        x = n//rows
        i = 0
        while i<n:
            matrix.append(encodedText[i:i+x])
            i+=x
        
        res = ""
        for i in range(len(matrix[0])) :
            for j in range(len(matrix)) :
                if i+j<len(matrix[0]):
                    res += matrix[j][i+j]
        
        i = len(res)-1
        while res[i]==" ":
            i-=1
        return res[:i+1]