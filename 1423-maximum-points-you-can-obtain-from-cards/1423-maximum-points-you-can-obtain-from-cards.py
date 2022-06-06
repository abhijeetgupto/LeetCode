class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        if len(cardPoints)==k:
            return sum(cardPoints)
        
        left = [0]
        right = [0]
        
        curr = 0
        for num in cardPoints:
            curr += num
            left.append(curr)
            
        curr=0
        for i in range(len(cardPoints)-1,-1,-1):
            curr += cardPoints[i]
            right.append(curr)
        
        
        res = 0
        for i in range(k+1):
            res = max(res, left[i] + right[k-i])
            
        return res
            