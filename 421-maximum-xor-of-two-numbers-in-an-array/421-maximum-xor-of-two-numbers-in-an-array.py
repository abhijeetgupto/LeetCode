class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        
        n = len(bin(max(nums)))-2
        root = {}
        def addWord(num):
            x = bin(num)[2:]
            word = "0"*(n-len(x)) + x
            curr = root
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr["*"] = num
        
        
        
        def checker(num):
            x = bin(num)[2:]
            word = "0"*(n-len(x)) + x
            curr = root
            for char in word:
                
                if char == "0":
                    if "1" in curr:
                        curr = curr["1"]
                        
                    elif "0" in curr:
                        curr = curr["0"]
            
                else:        
                    if "0" in curr:
                        curr = curr["0"]
                    
                    elif "1" in curr:
                        curr = curr["1"]
                    
            num2 = curr["*"]
            return num2^num
                    
            

        for num in nums:
            addWord(num)
        
        res = 0
        for num in nums:
            res = max(res, checker(num))
        
        return res
        