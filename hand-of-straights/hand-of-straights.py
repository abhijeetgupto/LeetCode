class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        
        
        if len(hand)%k!= 0:
            return False
        
        dic = dict(collections.Counter(hand))
        
        while dic :
            
            m = min(dic.keys())
            x = dic[m]
            
            for i in range(m,m+k):
                if i not in dic or dic[i] < x:
                    return False
                else:
                    dic[i] -= x
                    if dic[i] == 0 :
                        dic.pop(i)
        return True
        
        