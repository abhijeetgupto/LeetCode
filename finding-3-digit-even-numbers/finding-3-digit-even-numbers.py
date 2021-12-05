class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        res = set()
        for i in range(len(digits)) :
            if digits[i] != 0 :
                for j in range(len(digits)) :
                    for k in range(len(digits)) :
                        if i!=j and j!=k and i!=k and digits[k]%2 == 0:
                            res.add(int(str(digits[i])+str(digits[j])+str(digits[k])))
        return sorted(res)