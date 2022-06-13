class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        if brackets[0][0] >= income:
            return brackets[0][1]*income/100
        
        res= brackets[0][0]*brackets[0][1]/100
        income -= brackets[0][0]

        for i in range(1, len(brackets)):

            diff = brackets[i][0] - brackets[i-1][0]
            if diff > income:
                res += income*brackets[i][1]/100
                break
            else:
                res += diff* brackets[i][1]/100
                income -= diff
        
        return res
        