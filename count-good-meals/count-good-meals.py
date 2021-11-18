class Solution:
    def countPairs(self, arr: List[int]) -> int:
        
        if len(arr) < 2 :
            return 0
        
        power = [1,2]
        curr = 2
        arr.sort()
        m = arr[-1]+arr[-2]
        while curr <= m :
            curr*=2
            power.append(curr)
        
        
        dic = dict(collections.Counter(arr))
       
        count = 0
    
        for key in dic :
            for num in power :
                target = num-key
                if target == key :
                    n = dic[key]
                    count += (n)*(n-1)//2
                elif target > key :
                    if target in dic :
                        count += dic[key]*dic[target]
                    
        return count%(1000000007)
                
            