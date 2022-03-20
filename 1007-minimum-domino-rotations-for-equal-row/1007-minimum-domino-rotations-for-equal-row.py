class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(tops)
        temp = []
        for i in range(1,7):
            temp.append(tops.count(i) + bottoms.count(i))
        
        x = max(temp)
        if x < n :
            return -1
        
        vals  = []
        for i in range(6) :
            if temp[i]==x :
                vals.append(i+1)
        
        res = None
        while vals :
            top = vals.pop()
            flag = True
            for i in range(n) :
                if tops[i] != top and bottoms[i] != top :
                    flag = False
                    break
            if flag :
                res = n-max(tops.count(top), bottoms.count(top))
        
        if res is not None :
            return res
        return -1
                
        
        
        