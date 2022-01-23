class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        l = len(str(low))
        dic = {2: 12, 3 : 123, 4 : 1234, 5 : 12345, 6 : 123456, 7 : 1234567, 8 : 12345678, 9 : 123456789 }
        curr = dic[l]
        res = []
        while curr<low :
            s = str(curr)
            if s[-1] != "9" :
                curr += int("1"*len(str(curr)))
            else :
                try :
                    curr = dic[len(s)+1]
                except :
                    break
        if curr<low :
            return []
        while curr<=high :
            res.append(curr)
            s = str(curr)
            if s[-1] != "9" :
                curr += int("1"*len(str(curr)))
            else :
                try :
                    curr = dic[len(s)+1]
                except :
                    break
        return res
                